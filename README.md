# ipyvega

A Vega V3 / Vega-Lite V2 Jupyter display library

*Note* that the official [ipyvega](https://github.com/vega/ipyvega/tree/vega3)
now also supports Vega 3. It's adviced to use the official version.

## Installation

Install the python distribution with `pip`.

```bash
    pip install git+https://github.com/vmoret/ipyvega.git
```

Activate the Jupyter notebook extension

```bash
    jupyter nbextension enable --py vega
```

```bash
    cd packages\labextension\
    jupyter labextension link .
```

## Usage

```python
    import pandas as pd
    from vega import Vega

    Vega.from_file('bar.vg.json')

    df = pd.read_csv('some.csv', index_col=0)
    Vega({
        "$schema": "https://vega.github.io/schema/vega-lite/v2.0.json",
        ...
    }, df)
```
