# relpy

Python module for reliability computation

### Install with conda

The recommendation is to use Anaconda/Miniconda with your own environment for nmarkov.

```sh
conda create -n relpy python=3.6 jupyter numpy scipy matplotlib pybind11
conda activate relpy
conda install -c conda-forge pydotplus graphviz
pip install git+https://github.com/okamumu/relpy.git
```

For Jupyter, make the kernel for the environment `relpy`
```
conda activate relpy
ipython kernel install --user --name relpy
```

### Install with pip

```sh
pip install git+https://github.com/okamumu/relpy.git
```

Requriements:
- pybind11
- numpy
- scipy

Suggets:
- pydotplus (it requires graphviz)

