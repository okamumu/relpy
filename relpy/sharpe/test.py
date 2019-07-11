import io
import sys
import re
from antlr4 import *
from SHARPELexer import SHARPELexer
from SHARPEParser import SHARPEParser
from Listener import Listener

def main(argv):
    print('read ' + argv[1])
    f = open(argv[1], 'r')
    data = io.StringIO()
    for line in f:
        if not re.match(r"^\s*\*", line):
            data.write(line)
    f.close()
    
    input = InputStream(data.getvalue())
    lexer = SHARPELexer(input)
    stream = CommonTokenStream(lexer)
    parser = SHARPEParser(stream)
    listener = Listener()
    parser.addParseListener(listener)
    parser.prog()

if __name__ == '__main__':
    main(sys.argv)
