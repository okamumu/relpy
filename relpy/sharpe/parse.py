import os
import sys
from .Listener import *

def parse(filepath, envstr = 'env'):
    dirname, fname = os.path.split(filepath)
    try:
        return read_sharpe(fpath=filepath, envstr=envstr, header=True, dirname=dirname)
    except ParserException:
        return('Parser error: Please check the sharpe code')

if __name__ == '__main__':
    print(parse(sys.argv[1]))
