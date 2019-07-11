g++ -std=c++11 -Wall -shared -fPIC \
  -I pybind11/include -I marlib \
  `python3-config --cflags --ldflags` \
  relpy/src/nmarkov.cpp \
  -o relpy/nmarkov`python3-config --extension-suffix` \
  -l blas
