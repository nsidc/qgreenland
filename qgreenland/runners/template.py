# NOTE: wait to do templates til the end -- we'll probably need to recurse into
# the steps within each template. Do we have time for templates to be nestable?
# Should templates be able to reference other templates?
from qgreenland.util.luigi import LayerTask


class TemplateRunner(LayerTask):
    pass
