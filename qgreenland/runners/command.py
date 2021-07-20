import luigi

from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import run_ogr_command


def interpolate_args(
    args: List[str],
    **kwargs,
) -> List[str]:
    """Replace slugs in `args` with keys and values in `kwargs`."""
    # probably just .format()
    # TODO: COMMIT.

    breakpoint()
    pass


def command_runner(step: Step, *, input_dir: str, output_dir: str):
    """Run a shell command.

    Interpolate the following special slugs:

        {output_dir} - self.output()
        {input_dir} - self.input()  # [.path?]
    """
    breakpoint()

    # TODO: Some better data structure; this access is confusing.
    command_args = step[0]

    interpolate_args(
        command_args,
        input_dir=input_dir,
        output_dir=output_dir,
    )

    subprocess(command_args)


# class CommandRunner(LayerTask):
#     command_args = luigi.ListParameter()
#    
#     def output(self):
#         return luigi.LocalTarget(
#             Path(self.outdir) / 
#             f'command-{self.command_args[0]}',
#         )
# 
#     def run(self):
#         # TODO: Replace {input}, {output} slugs in commands
# 
#         run_ogr_command(self.command_args)
