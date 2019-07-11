import ipdb
import sys
from antlr4 import *
from QueryLexer import QueryLexer
from QueryParser import QueryParser
from MyQueryListener import MyQueryListener

def main(argv):
    print('read ' + argv[1])
    input = FileStream(argv[1])
    lexer = QueryLexer(input)
    stream = CommonTokenStream(lexer)
    parser = QueryParser(stream)
    listener = MyQueryListener()
#    ipdb.set_trace()
    parser.addParseListener(listener)
    parser.prog()

if __name__ == '__main__':
    main(sys.argv)
