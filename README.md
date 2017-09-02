# ipyvega
A Vega V3 / Vega-Lite V2 Jupyter display library

## Installation

To install use pip:

```bash
    pip install dist\ipyvega-*.tar.gz
    jupyter nbextension enable --py ipyvega
```

## Usage

```python
    from vega import Vega
    Vega.from_file('bar.vg.json')
```
