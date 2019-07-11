g++ -std=c++11 -Wall -shared -fPIC \
  -I pybind11/include \
  -I marlib \
  -I include \
  `python3-config --cflags --ldflags` \
  src/nmarkov.cpp \
  -o nmarkov`python3-config --extension-suffix` \
  -l blas