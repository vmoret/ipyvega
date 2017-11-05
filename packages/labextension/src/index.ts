import {
  JSONObject
} from '@phosphor/coreutils';

import {
  IRenderMime
} from '@jupyterlab/rendermime-interfaces';

import {
  Widget
} from '@phosphor/widgets';

/**
 * Import vega-embed in this manner due to how it is exported.
 */
import _embed = require('vega-embed');
const embed = _embed.default;

import '../style/index.css';


/**
 * The MIME type for Vega V3 and Vega-Lite V2
 */
const MIME_TYPE = 'application/vnd.vega.v3+json';

/**
 * The CSS class to add to the Vega V3 and Vega-Lite V2 widget.
 */
const CSS_CLASS = 'jp-RenderedVega';

/**
 * The fileType name for Vega V3 and Vega-Lite V2.
 */
const FILE_TYPE = 'vega-v3';


/**
 * A widget for rendering Vega V3 / Vega-Lite V2.
 */
export
class OutputWidget extends Widget implements IRenderMime.IRenderer {
  /**
   * Construct a new output widget.
   */
  constructor(options: IRenderMime.IRendererOptions) {
    super();

    this.addClass(CSS_CLASS);
    this._mimeType = options.mimeType;
  }

  /**
   * Render Vega / Vega-Lite into this widget's node.
   */
  renderModel(model: IRenderMime.IMimeModel): Promise<void> {
    const data: JSONObject = model.data[this._mimeType] as JSONObject;
    const options: JSONObject = data.$options as JSONObject || {};
    const spec = Object.keys(data)
      .filter(x => x !== '$options')
      .reduce<JSONObject>(
        (prev: JSONObject, curr: string): JSONObject =>
          (prev[curr] = data[curr], prev)
        , {});

    return embed(this.node as HTMLBaseElement, spec, options)
      .then(({view, spec}) => {
        return view.toSVG();
      })
      .then(svg => {
        (<JSONObject>(model.data))['image/svg+xml'] = svg;
      });
  }

  private _mimeType: string;
}


/**
 * A mime renderer factory for Vega V3 / Vega-Lite V2 data.
 */
export
const rendererFactory: IRenderMime.IRendererFactory = {
  safe: true,
  mimeTypes: [MIME_TYPE],
  createRenderer: options => new OutputWidget(options)
};


const extension: IRenderMime.IExtension = {
  id: 'VEGA3',
  rendererFactory,
  rank: 0,
  dataType: 'json',
  documentWidgetFactoryOptions: [{
    name: 'Vega V3',
    modelName: 'text',
    primaryFileType: FILE_TYPE,
    fileTypes: [FILE_TYPE, 'json'],
    defaultFor: [FILE_TYPE]
  }],
  fileTypes: [{
    name: FILE_TYPE,
    mimeTypes: [MIME_TYPE],
    fileFormat: 'text',
    extensions: ['.vg3', '.vg3.json', '.vl2', '.vl2.json'],
    iconClass: 'jp-MaterialIcon jp-VegaIcon'
  }]
};

export default extension;
