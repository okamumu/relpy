FROM jupyter/datascience-notebook

USER root
RUN apt-get -y update &&\
        apt-get install -y \
            libc-bin \
            libopenblas-base

USER jovyan
RUN conda install -c anaconda openblas
RUN pip install z3-solver pybind11
