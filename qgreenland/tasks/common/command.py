from pathlib import Path

import luigi

from qgreenland.constants import TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import find_single_file_by_ext, run_ogr_command, temporary_path_dir


class Commands(LayerTask):
    task_type = TaskType.WIP
    commands = luigi.ListParameter()

    def output(self):
        return luigi.LocalTarget(Path(self.outdir) / 'commands')

    def run(self):
        with temporary_path_dir(self.output()) as tmp_dir:
            tmp_dir_path = Path(tmp_dir)

            input_path = find_single_file_by_ext(
                self.input().path,
                ext=self.layer_cfg['file_type']
            )
            output_path = tmp_dir_path / f"{self.layer_id}{self.layer_cfg['file_type']}"
            for command in self.commands:
                interpolate_kwargs = {
                    'INPUT': input_path,
                    'OUTDIR': tmp_dir_path,
                    'OUTPUT': output_path,
                }

                interpolated_command = [
                    element.format(**interpolate_kwargs) if isinstance(element, str) else str(element)
                    for element in command
                ]

                run_ogr_command(interpolated_command)

            # cleanup intermediate files. Downstream jobs only expect one.
            for tmp_dir_file in tmp_dir_path.iterdir():
                if tmp_dir_file == output_path:
                    continue

                tmp_dir_file.unlink()
