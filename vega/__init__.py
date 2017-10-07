"""
Jupyter Vega / Vega-Lite extension.
"""
from ._version import version_info, __version__

from ._vega import Vega, VegaLite
from ._data import VegaData


# Running `npm run build` will create static resources in the static
# directory of this Python package (and create that directory if necessary).

def _jupyter_nbextension_paths():
    return [dict(
        section='notebook',
        # the path is relative to the `ipyvega` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="ipyvega",
        # _also_ in the `nbextension/` namespace
        require="ipyvega/extension"
    )]
