from qgreenland.models.config.step import AnyStep


def steps_to_provenance_text(steps: list[AnyStep]) -> str:
    steps_as_text = [step.provenance for step in steps]

    return '\n\n'.join(steps_as_text)
