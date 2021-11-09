from jinja2 import Template

from qgreenland.constants.paths import TEMPLATES_DIR


def load_template(fn: str) -> Template:
    """Load template from TEMPLATES_DIR.

    TODO: Do this the documented way, i.e. using a jinja Environment?

        jinja_env = Environment(
            loader=PackageLoader(
                "qgreenland",
                package_path="ancillary/templates",
            ),
        )
    """
    template_path = TEMPLATES_DIR / fn

    with open(template_path, 'r') as f:
        template_str = ''.join(f.readlines())

    return Template(template_str)
