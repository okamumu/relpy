import io
import sys
import re
from antlr4 import *
from collections import deque
from .SHARPEParser import SHARPEParser
from .SHARPEListener import SHARPEListener
from .SHARPELexer import *

class ParserException(Exception):
    pass

def read_sharpe(fpath, envstr, header, dirname):
    with open(fpath, 'r') as f:
        data = io.StringIO()
        for line in f:
            if not re.match(r"^\s*\*", line):
                data.write(re.sub(r'lambda', "plambda", line))
            else:
                data.write('\n')
    try:
        input = InputStream(data.getvalue())
        lexer = SHARPELexer(input)
        stream = CommonTokenStream(lexer)
        parser = SHARPEParser(stream)
        listener = Listener(envstr = envstr, header = header, dirname = dirname)
        parser.addParseListener(listener)
        parser.prog()
        return listener.getvalue()
    except ParserException:
        raise ParserException


class Listener(SHARPEListener):
    def __init__(self, envstr = 'env', header = True, dirname = './'):
        self.stack = deque([])
        self.f = io.StringIO()
        self.modeltemp = io.StringIO()
        self.error = False
        self.bindent = '     '
        self.params = set()
        self.env = io.StringIO()
        self.header = header
        self.envstr = envstr
        self.dirname = dirname

    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        x = self.stack.pop()
        return x

    def getvalue(self):
        return self.f.getvalue() + self.env.getvalue() + self.modeltemp.getvalue()

    def enterProg(self, ctx:SHARPEParser.ProgContext):
        if self.header == True:
            self.f.write('import relpy\n')
            self.f.write('{} = relpy.Env()\n'.format(self.envstr))

    def exitProg(self, ctx:SHARPEParser.ProgContext):
        if ctx.exception != None:
            raise ParserException
    
    def exitIncludeStatement(self, ctx:SHARPEParser.IncludeStatementContext):
        fpath = self.dirname + '/'
        for i in range(1,len(ctx.children)):
            fpath = fpath + ctx.children[i].getText()
        print('include ' + fpath)
        self.f.write(read_sharpe(fpath=fpath, envstr=self.envstr, header=False, dirname=self.dirname))
        pass

    def exitBindStatement(self, ctx:SHARPEParser.BindStatementContext):
        pass

    def exitBindDecleration(self, ctx:SHARPEParser.BindDeclerationContext):
        if ctx.type == 1: # literal
            label = ctx.children[0].getText()
            data = ctx.children[1].getText()
            self.f.write('{label} = relpy.Parameter("{label}")\n'.format(label=label))
            self.env.write('{env}[{label}] = {data}\n'.format(env=self.envstr, label=label, data=data))
        elif ctx.type == 2: # expr
            label = ctx.children[0].getText()
            x = self.pop()
            self.f.write('def bind_{model}({params}):\n'.format(model=label, params=', '.join(self.params)))
            self.f.write(self.bindent + 'return {}\n'.format(x))
            self.f.write('\n')
            self.modeltemp.write('# {model} = bind_{model}({params})\n'.format(model=label, params=', '.join(self.params)))
            self.params = set()

    def exitBindBlock(self, ctx:SHARPEParser.BindBlockContext):
        pass

    def exitMarkovBlock(self, ctx:SHARPEParser.MarkovBlockContext):
        self.f.write('def ctmc_{model}({params}):\n'.format(model=self.ctmc, params=', '.join(self.params)))
        self.f.write(self.bindent + '{} = relpy.CTMC("{}")\n'.format(self.ctmc, self.ctmc))
        self.f.write(self.markovmodel.getvalue())
        self.f.write(self.bindent + 'return {}\n'.format(self.ctmc))
        self.f.write('\n')
        self.modeltemp.write('# {model} = ctmc_{model}({params})\n'.format(model=self.ctmc, params=', '.join(self.params)))
        self.params = set()

    def exitMarkovBlockDecleration(self, ctx:SHARPEParser.MarkovBlockDeclerationContext):
        self.markovmodel = io.StringIO()
        self.ctmc = ctx.children[1].getText()
        self.params = set()

    def exitMarkovTransDecrelation(self, ctx:SHARPEParser.MarkovTransDecrelationContext):
        s = ctx.children[0].getText()
        d = ctx.children[1].getText()
        expr = self.pop()
        self.markovmodel.write(self.bindent + '{}.add_trans("{}", "{}", {})\n'.format(self.ctmc, s, d, expr))

    def exitMarkovRwdStateDecrelation(self, ctx:SHARPEParser.MarkovRwdStateDecrelationContext):
        s = ctx.children[0].getText()
        expr = self.pop()
        self.markovmodel.write(self.bindent + '{}.add_reward("{}", {})\n'.format(self.ctmc, s, expr))

    def exitMarkovInitStateDecrelation(self, ctx:SHARPEParser.MarkovInitStateDecrelationContext):
        s = ctx.children[0].getText()
        expr = self.pop()
        self.markovmodel.write(self.bindent + '{}.add_init("{}", {})\n'.format(self.ctmc, s, expr))

    def enterFtreeBlock(self, ctx:SHARPEParser.FtreeBlockContext):
        pass

    def exitFtreeBlock(self, ctx:SHARPEParser.FtreeBlockContext):
        self.f.write('def ftree_{model}({params}):\n'.format(model=self.ft, params=', '.join(self.params)))
        self.f.write(self.ftreemodel.getvalue())
        self.f.write(self.bindent + 'return relpy.FTEvent({})\n'.format(self.fttop))
        self.f.write('\n')
        self.modeltemp.write('# {model} = ftree_{model}({params})\n'.format(model=self.ft, params=', '.join(self.params)))
        self.params = set()

    def exitFtreeBlockDecleration(self, ctx:SHARPEParser.FtreeBlockDeclerationContext):
        self.ftreemodel = io.StringIO()
        self.ft = ctx.children[1].getText()
        self.params = set()

    def exitFtreeRepeatDecrelation(self, ctx:SHARPEParser.FtreeRepeatDecrelationContext):
        x = ctx.children[1].getText()
        expr = self.pop()
        self.ftreemodel.write(self.bindent + '{} = relpy.FTEvent({})\n'.format(x, expr))
        self.fttop = x

    def exitFtreeBasicDecrelation(self, ctx:SHARPEParser.FtreeBasicDecrelationContext):
        x = ctx.children[1].getText()
        expr = self.pop()
        self.ftreemodel.write(self.bindent + '{} = relpy.FTEvent({})\n'.format(x, expr))
        self.fttop = x

    def exitExpDistribution(self, ctx:SHARPEParser.ExpDistributionContext):
        x = self.pop()
        self.push('relpy.ExpDist({}, _time)'.format(x))
        self.params.add('_time')

    def exitProbDistribution(self, ctx:SHARPEParser.ProbDistributionContext):
        x = ctx.children[2].getText()
        pass

    def exitCdfDistribution(self, ctx:SHARPEParser.CdfDistributionContext):
        x = ctx.children[2].getText()
        self.push(x)
        self.params.add(x)

    def exitFtreeAndDecrelation(self, ctx:SHARPEParser.FtreeAndDecrelationContext):
        x = ctx.children[1].getText()
        node = [ ctx.children[i].getText() for i in range(2,len(ctx.children))]
        self.ftreemodel.write(self.bindent + '{} = {}\n'.format(x, ' & '.join(node)))
        self.fttop = x

    def exitFtreeOrDecrelation(self, ctx:SHARPEParser.FtreeOrDecrelationContext):
        x = ctx.children[1].getText()
        node = [ ctx.children[i].getText() for i in range(2,len(ctx.children))]
        self.ftreemodel.write(self.bindent + '{} = {}\n'.format(x, ' | '.join(node)))
        self.fttop = x

    def exitFtreeKofNDecrelation(self, ctx:SHARPEParser.FtreeKofNDecrelationContext):
        x = ctx.children[1].getText()
        node = [ ctx.children[i].getText() for i in range(6,len(ctx.children))]
        n = self.pop()
        k = self.pop()
        self.ftreemodel.write(self.bindent + '{f} = relpy.FTKofn({k}.eval({env}), {n}.eval({env}), [{params}])\n'.format(f=x, k=k, n=n, env=self.envstr, params=', '.join(node)))
        self.fttop = x

    def exitExpr(self, ctx:SHARPEParser.ExprContext):
        if ctx.type == 1:
            x = self.pop()
            if ctx.op.text == '-':
                self.push('-({})'.format(x))
        elif ctx.type == 2: # *, /
            r = self.pop()
            l = self.pop()
            if ctx.op.text == '*':
                self.push('({} * {})'.format(l, r))
            elif ctx.op.text == '/':
                self.push('({} / {})'.format(l, r))
            else:
                pass
        elif ctx.type == 3: # +, -
#            ipdb.set_trace()
            r = self.pop()
            l = self.pop()
            if ctx.op.text == '+':
                self.push('({} + {})'.format(l, r))
            elif ctx.op.text == '-':
                self.push('({} - {})'.format(l, r))
            else:
                pass
        elif ctx.type == 4: # func
            pass
        elif ctx.type == 5: # literal
            self.push('relpy.Const({})'.format(ctx.children[0].getText()))
            pass
        elif ctx.type == 6: # id
            self.push('{}'.format(ctx.children[0].getText()))
            self.params.add(ctx.children[0].getText())
            pass
        elif ctx.type == 7: # pa
            pass
        else:
            pass

    def exitExp_function(self, ctx:SHARPEParser.Exp_functionContext):
        x = str(self.pop())
        self.push('relpy.exp({})'.format(x))

    def exitMarkovprob_function(self, ctx:SHARPEParser.Markovprob_functionContext):
        x = ctx.children[2].getText()
        y = ctx.children[4].getText()
        self.push('relpy.CTMCStProb({},["{}"])'.format(x,y))
        self.params.add(x)

    def exitMarkovexrss_function(self, ctx:SHARPEParser.Markovexrss_functionContext):
        x = ctx.children[2].getText()
        self.push('relpy.CTMCExrss({})'.format(x))
        self.params.add(x)

    def exitFtsysprob_function(self, ctx:SHARPEParser.Ftsysprob_functionContext):
        x = ctx.children[2].getText()
        self.push(x)
        self.params.add(x)
