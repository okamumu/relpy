import io
import sys
from antlr4 import *
from collections import deque
from .SHARPEParser import SHARPEParser
from .SHARPEListener import SHARPEListener

class ParserException(Exception):
    pass

class Listener(SHARPEListener):
    def __init__(self):
        self.stack = deque([])
        self.f = io.StringIO()
        self.error = False
        self.bindent = '     '
        self.params = set()

    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        x = self.stack.pop()
        return x

    def getvalue(self):
        return self.f.getvalue()

    def enterProg(self, ctx:SHARPEParser.ProgContext):
        self.f.write('import relpy\n')
        self.f.write('env = {}\n')
        self.f.write('cache = {}\n')
        pass

    def exitProg(self, ctx:SHARPEParser.ProgContext):
        if ctx.exception != None:
            raise ParserException
    
    def exitBindDecleration(self, ctx:SHARPEParser.BindDeclerationContext):
        if ctx.type == 1: # literal
            label = ctx.children[0].getText()
            data = ctx.children[1].getText()
            self.f.write('{} = relpy.Parameter("{}")\n'.format(label, label))
            self.f.write('env[{}] = {}\n'.format(label, data))
        elif ctx.type == 2: # expr
            label = ctx.children[0].getText()
            x = self.pop()
            self.f.write('{} = {}\n'.format(label, x))

    def exitMarkovBlock(self, ctx:SHARPEParser.MarkovBlockContext):
        self.f.write('class ctmc_{}(relpy.CTMC):\n'.format(self.ctmc))
        self.f.write(self.bindent + 'def __init__({}):\n'.format(','.join(self.params)))
        self.f.write(self.markovmodel.getvalue())
        self.f.write('\n')
        pass

    def exitMarkovBlockDecleration(self, ctx:SHARPEParser.MarkovBlockDeclerationContext):
        self.markovmodel = io.StringIO()
        self.ctmc = ctx.children[1].getText()
        self.params = set()
#        self.f.write('{} = relpy.CTMC("{}")\n'.format(self.ctmc, self.ctmc))

    def exitMarkovTransDecrelation(self, ctx:SHARPEParser.MarkovTransDecrelationContext):
        s = ctx.children[0].getText()
        d = ctx.children[1].getText()
        expr = self.pop()
        self.markovmodel.write(self.bindent + self.bindent + 'self.add_trans("{}", "{}", {})\n'.format(s, d, expr))

    def exitMarkovRwdStateDecrelation(self, ctx:SHARPEParser.MarkovRwdStateDecrelationContext):
        s = ctx.children[0].getText()
        expr = self.pop()
        self.markovmodel.write(self.bindent + self.bindent + 'self.add_reward("{}", {})\n'.format(s, expr))

    def exitMarkovInitStateDecrelation(self, ctx:SHARPEParser.MarkovInitStateDecrelationContext):
        s = ctx.children[0].getText()
        expr = self.pop()
        self.markovmodel.write(self.bindent + self.bindent + 'self.add_init("{}", {})\n'.format(s, expr))

    def enterFtreeBlock(self, ctx:SHARPEParser.FtreeBlockContext):
        pass

    def exitFtreeBlock(self, ctx:SHARPEParser.FtreeBlockContext):
        self.f.write('class ftree_{}(relpy.FaultTree):\n'.format(self.ft))
        self.f.write(self.bindent + 'def __init__({}):\n'.format(','.join(self.params)))
        self.f.write(self.ftreemodel.getvalue())
        self.f.write('\n')
        self.f.write(self.bindent + 'def eval(self, env):\n')
        self.f.write(self.bindent + self.bindent + 'return {ft}.eval(env)\n'.format(ft=self.fttop))
        self.f.write('\n')
        self.f.write(self.bindent + 'def deriv(self, env, p):\n')
        self.f.write(self.bindent + self.bindent + 'return {ft}.deriv(env, p)\n'.format(ft=self.fttop))
        self.f.write('\n')
        self.f.write(self.bindent + 'def deriv2(self, env, p1, p2):\n')
        self.f.write(self.bindent + self.bindent + 'return {ft}.deriv2(env, p1, p2)\n'.format(ft=self.fttop))
        self.f.write('\n')
        pass

    def exitFtreeBlockDecleration(self, ctx:SHARPEParser.FtreeBlockDeclerationContext):
        self.ftreemodel = io.StringIO()
        self.ft = ctx.children[1].getText()
        self.params = set()

    def exitFtreeRepeatDecrelation(self, ctx:SHARPEParser.FtreeRepeatDecrelationContext):
        x = ctx.children[1].getText()
        expr = self.pop()
        self.ftreemodel.write(self.bindent + self.bindent + '{} = relpy.FTEvent({})\n'.format(x, expr))
        self.fttop = x

    def exitFtreeBasicDecrelation(self, ctx:SHARPEParser.FtreeBasicDecrelationContext):
        x = ctx.children[1].getText()
        expr = self.pop()
        self.ftreemodel.write(self.bindent + self.bindent + '{} = relpy.FTEvent({})\n'.format(x, expr))
        self.fttop = x

    def exitFtreeAndDecrelation(self, ctx:SHARPEParser.FtreeAndDecrelationContext):
        x = ctx.children[1].getText()
        node = [ ctx.children[i].getText() for i in range(2,len(ctx.children))]
        self.ftreemodel.write(self.bindent + self.bindent + '{} = {}\n'.format(x, '&'.join(node)))
        self.fttop = x

    def exitFtreeOrDecrelation(self, ctx:SHARPEParser.FtreeOrDecrelationContext):
        x = ctx.children[1].getText()
        node = [ ctx.children[i].getText() for i in range(2,len(ctx.children))]
        self.ftreemodel.write(self.bindent + self.bindent + '{} = {}\n'.format(x, '|'.join(node)))
        self.fttop = x

    def exitFtreeKofNDecrelation(self, ctx:SHARPEParser.FtreeKofNDecrelationContext):
        x = ctx.children[1].getText()
        node = [ ctx.children[i].getText() for i in range(6,len(ctx.children))]
        n = self.pop()
        k = self.pop()
        self.ftreemodel.write(self.bindent + self.bindent + '{} = relpy.FTKofn({}.eval(env,cache), {}.eval(env,cache), [{}])\n'.format(x, k, n, ','.join(node)))
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
        x = self.pop()
        self.push('relpy.exp({})'.format(x))

    def exitMarkovprob_function(self, ctx:SHARPEParser.Markovprob_functionContext):
        x = ctx.children[2]
        y = ctx.children[4]
        self.push('relpy.CTMCStProb({},["{}"])'.format(x,y))
        # self.params.add(x)

    def exitMarkovexrss_function(self, ctx:SHARPEParser.Markovexrss_functionContext):
        x = ctx.children[2]
        self.push('relpy.CTMCExrss({})'.format(x))
        # self.params.add(x)

    def exitFtprob_function(self, ctx:SHARPEParser.Ftprob_functionContext):
        pass

    def exitFtsysprob_function(self, ctx:SHARPEParser.Ftsysprob_functionContext):
        x = ctx.children[2]
        self.push(x)
        # self.params.add(x)
