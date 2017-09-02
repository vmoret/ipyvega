/**
 * This file contains the javascript that is run when the notebook is loaded.
 * It contains some requirejs configuration and the `load_ipython_extension`
 * which is required for any notebook extension.
 */

import {
  render_cells, register_renderer
} from './renderer';

/**
 * Configure requirejs.
 */
if (window.require) {
  window.require.config({
    map: {
      '*': {
        'ipyvega': 'nbextensions/ipyvega/index'
      }
    }
  });
}

/**
 * Export the required load_ipython_extention.
 */
export function load_ipython_extension() {
  define(
    ['base/js/namespace'],
    (Jupyter) => {
      const { notebook } = Jupyter;
      register_renderer(notebook);
      render_cells(notebook);
    }
  );
}
