# vmoret/ipyvega-lab

A Vega V3 / Vega-Lite V2 JupyterLab MIME renderer extension.

Created as the [MIME render extension](https://github.com/jupyterlab/jupyterlab/tree/master/packages/vega2-extension) shipping with JupyterLab is Vega V2 based, which prevents me from using features available in Vega V3 / Vega-Lite V2.


## Prerequisites

* JupyterLab

## Installation

```bash
jupyter labextension install ipyvega-lab
```

## Development

For a development install (requires npm version 4 or later), do the following in
the repository directory:

```bash
npm install
jupyter labextension link .
```

To rebuild the package and the JupyterLab app:

```bash
npm run build
jupyter lab build
```
