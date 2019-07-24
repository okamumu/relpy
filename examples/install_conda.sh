#!/bin/sh

conda install -y numpy scipy matplotlib jupyter pybind11
conda install -c conda-forge pydotplus
pip install git+https://github.com/okamumu/relpy.git
