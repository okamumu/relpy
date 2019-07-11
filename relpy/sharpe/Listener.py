from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SHARPEParser import SHARPEParser
else:
    from SHARPEParser import SHARPEParser
from SHARPEListener import SHARPEListener
from collections import deque

from pySHARPE.expr import *
from pySHARPE.ftree import *
from pySHARPE.markov import *

class Listener(SHARPEListener):
    def __init__(self):
        self.stack = deque([])

    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        x = self.stack.pop()
        return x

    def enterProg(self, ctx:SHARPEParser.ProgContext):
        pass

    def exitProg(self, ctx:SHARPEParser.ProgContext):
        pass

    def exitBindDecleration(self, ctx:SHARPEParser.BindDeclerationContext):
        label = ctx.children[0].getText()
        x = self.pop()
        print('{} = {}'.format(label, x))

    def exitMarkovBlock(self, ctx:SHARPEParser.MarkovBlockContext):
        self.markov.toR()

    def exitMarkovBlockDecleration(self, ctx:SHARPEParser.MarkovBlockDeclerationContext):
        x = ctx.children[1].getText()
        self.ctmc = CTMC(x)

    def exitMarkovTransDecrelation(self, ctx:SHARPEParser.MarkovTransDecrelationContext):
        s = ctx.children[0].getText()
        d = ctx.children[1].getText()
        expr = self.pop()
        self.ctmc.add_trans(s, d, expr)

    def exitMarkovRwdStateDecrelation(self, ctx:SHARPEParser.MarkovRwdStateDecrelationContext):
        s = ctx.children[0].getText()
        expr = self.pop()
        self.ctmc.add_reward(s, expr)

    def exitMarkovInitStateDecrelation(self, ctx:SHARPEParser.MarkovInitStateDecrelationContext):
        s = ctx.children[0].getText()
        expr = self.pop()
        self.ctmc.add_init(s, expr)

    def enterFtreeBlock(self, ctx:SHARPEParser.FtreeBlockContext):
        pass

    def exitFtreeBlock(self, ctx:SHARPEParser.FtreeBlockContext):
        self.ft.set_top(self.fttop)
        self.ft.toR()

    def exitFtreeBlockDecleration(self, ctx:SHARPEParser.FtreeBlockDeclerationContext):
        x = ctx.children[1].getText()
        self.ft = x

    def exitFtreeRepeatDecrelation(self, ctx:SHARPEParser.FtreeRepeatDecrelationContext):
        x = ctx.children[1].getText()
        expr = self.pop()
        self.ft.add_event_gates(x, expr)

    def exitFtreeBasicDecrelation(self, ctx:SHARPEParser.FtreeBasicDecrelationContext):
        x = ctx.children[1].getText()
        expr = self.pop()
        self.ft.add_event_gates(x, expr)
        self.fttop = x

    def exitFtreeAndDecrelation(self, ctx:SHARPEParser.FtreeAndDecrelationContext):
        x = ctx.children[1].getText()
        node = [ ctx.children[i].getText() for i in range(2,len(ctx.children))]
        self.ft.add_and_gates(x, node)
        self.fttop = x

    def exitFtreeOrDecrelation(self, ctx:SHARPEParser.FtreeOrDecrelationContext):
        x = ctx.children[1].getText()
        node = [ ctx.children[i].getText() for i in range(2,len(ctx.children))]
        self.ft.add_or_gates(x, node)
        self.fttop = x

    def exitFtreeKofNDecrelation(self, ctx:SHARPEParser.FtreeKofNDecrelationContext):
        x = ctx.children[1].getText()
        node = [ ctx.children[i].getText() for i in range(2,len(ctx.children))]
        self.ft.add_kofn_gates(x, node)
        self.fttop = x

    def exitExpr(self, ctx:SHARPEParser.ExprContext):
        if ctx.type == 1:
            x = self.pop()
            if ctx.op.text == '-':
                self.push('FTNot({})'.format(x))
        elif ctx.type == 2: # *, /
#            ipdb.set_trace()
            r = self.pop()
            l = self.pop()
            if ctx.op.text == '*':
                self.push('MulExpr$new({}, {})'.format(l, r))
            elif ctx.op.text == '/':
                self.push('DivExpr$new({}, {})'.format(l, r))
            else:
                pass
        elif ctx.type == 3: # +, -
#            ipdb.set_trace()
            r = self.pop()
            l = self.pop()
            if ctx.op.text == '+':
                self.push('PlusExpr$new({}, {})'.format(l, r))
            elif ctx.op.text == '-':
                self.push('MinusExpr$new({}, {})'.format(l, r))
            else:
                pass
        elif ctx.type == 4: # func
            pass
        elif ctx.type == 5: # literal
            self.push('expression({})'.format(ctx.children[0].getText()))
            pass
        elif ctx.type == 6: # id
            self.push('Expr$new(expression({}))'.format(ctx.children[0].getText()))
            pass
        elif ctx.type == 7: # pa
            pass
        else:
            pass

    def exitExp_function(self, ctx:SHARPEParser.Exp_functionContext):
        x = self.pop()
        self.push('ExpExpr$new({})'.format(x))

    def exitMarkovprob_function(self, ctx:SHARPEParser.Markovprob_functionContext):
        x = ctx.children[2]
        y = ctx.children[4]
        self.push('MarkovProb$new({},"{}")'.format(x,y))

    def exitMarkovexrss_function(self, ctx:SHARPEParser.Markovexrss_functionContext):
        x = ctx.children[2]
        self.push('MarkovExrss$new({})'.format(x))

    def exitFtprob_function(self, ctx:SHARPEParser.Ftprob_functionContext):
        pass

    def exitFtsysprob_function(self, ctx:SHARPEParser.Ftsysprob_functionContext):
        x = ctx.children[2]
        self.push(x)
