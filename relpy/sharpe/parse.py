import io
import sys
import re
from antlr4 import *
from .SHARPELexer import *
from .SHARPEParser import *
from .Listener import *

def parse(fname):
    with open(fname, 'r') as f:
        data = io.StringIO()
        for line in f:
            if not re.match(r"^\s*\*", line):
                data.write(re.sub(r'lambda', "plambda", line))
    try:
        input = InputStream(data.getvalue())
        lexer = SHARPELexer(input)
        stream = CommonTokenStream(lexer)
        parser = SHARPEParser(stream)
        listener = Listener()
        parser.addParseListener(listener)
        parser.prog()
        return listener.getvalue()
    except ParserException:
        return('Parser error: Please check the sharpe code')

if __name__ == '__main__':
    print(parse(sys.argv[1]))
