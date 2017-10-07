"""
Provides a display class to display Vega visualizations in the Jupyter Notebook
and IPython kernel.
"""

from traitlets import Dict, Unicode, HasTraits
from IPython.display import display

from ._spec import VegaSpec
from ._mixins import FromFileMixin, FromUrlMixin, FromTemplateMixin

# The MIME type for Vega + Vega-Lite.
MIME_TYPE = 'application/vnd.vega.v3+json'


class VegaBase(HasTraits):
    """
    A display class to display Vega/VegaLite visualizations in the Jupyter
    Notebook and IPython kernel.

    VegaBase expects a spec (a JSON-able dict) and data (dict) argument not
    already-serialized JSON strings.

    Scalar types (None, number, string) are not allowed, only dict containers.
    """

    spec = Dict({})
    options = Dict({'actions': False})
    metadata = Dict({})
    mode = Unicode('')

    def __init__(self, spec, data=None, options=None, metadata=None, size=None):
        self.spec = VegaSpec(spec, data=data, size=size)
        self.options = options or self.options
        self.metadata = metadata or self.metadata
        super().__init__()

    def _ipython_display_(self):
        """Displays object in notebook."""

        # mixin `options` in the spec
        spec = self.spec.copy()
        spec['$options'] = self.options

        # define display bundle objects
        bundle = {
            MIME_TYPE: spec,
            'text/plain': str(self)
        }

        # display objects
        display(bundle, metadata=self.metadata, raw=True)

        
def _ensure_schema(spec, schema):
    """
    Ensures there is a '$schema' key present in a Vega/VegaLite specificiation.
    
    Parameters
    ----------
    spec: Dict
        the specificiation to check
    schema: Unicode
        the schema to use when no '$schema' key was present
    """
    return ({'$schema': schema, **spec} 
            if len(schema) != 0 and '$schema' not in spec 
            else spec)


class Vega(VegaBase, FromFileMixin, FromUrlMixin, FromTemplateMixin):
    """
    A display class to display Vega visualizations in the Jupyter Notebook and
    IPython kernel.

    Vega expects a spec (a JSON-able dict) and data (dict) argument not
    already-serialized JSON strings.

    Scalar types (None, number, string) are not allowed, only dict containers.
    """

    def __init__(self, spec, data=None, options=None, metadata=None, size=None):
        _spec = _ensure_schema(spec, 
                               'https://vega.github.io/schema/vega/v3.0.json')
        super().__init__(_spec, data=data, options=options, metadata=metadata,
                         size=size)
    
    def __str__(self):
        return 'A Vega Plot'


class VegaLite(VegaBase, FromFileMixin, FromUrlMixin, FromTemplateMixin):
    """
    A display class to display Vega-Lite visualizations in the Jupyter Notebook
    and IPython kernel.

    VegaLite expects a spec (a JSON-able dict) and data (dict) argument not
    already-serialized JSON strings.

    Scalar types (None, number, string) are not allowed, only dict containers.
    """

    def __init__(self, spec, data=None, options=None, metadata=None, size=None):
        _spec = _ensure_schema(spec, 
                               'https://vega.github.io/schema/vega-lite/v2.json')
        super().__init__(_spec, data=data, options=options, metadata=metadata,
                         size=size)
    
    def __repr__(self):
        return 'A Vega-Lite Plot'
