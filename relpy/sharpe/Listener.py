import io
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SHARPEParser import SHARPEParser
else:
    from SHARPEParser import SHARPEParser
from SHARPEListener import SHARPEListener
from collections import deque

class Listener(SHARPEListener):
    def __init__(self):
        self.stack = deque([])
        self.f = io.StringIO()

    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        x = self.stack.pop()
        return x

    def enterProg(self, ctx:SHARPEParser.ProgContext):
        pass

    def exitProg(self, ctx:SHARPEParser.ProgContext):
        print(self.f.getvalue())
        pass

    def exitBindDecleration(self, ctx:SHARPEParser.BindDeclerationContext):
        # label = ctx.children[0].getText()
        # x = self.pop()
        # self.f.write('{} = {}\n'.format(label, x))
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
        pass

    def exitMarkovBlockDecleration(self, ctx:SHARPEParser.MarkovBlockDeclerationContext):
        self.ctmc = ctx.children[1].getText()
        self.f.write('{} = relpy.CTMC("{}")\n'.format(self.ctmc, self.ctmc))

    def exitMarkovTransDecrelation(self, ctx:SHARPEParser.MarkovTransDecrelationContext):
        s = ctx.children[0].getText()
        d = ctx.children[1].getText()
        expr = self.pop()
        self.f.write('{}.add_trans("{}", "{}", {})\n'.format(self.ctmc, s, d, expr))

    def exitMarkovRwdStateDecrelation(self, ctx:SHARPEParser.MarkovRwdStateDecrelationContext):
        s = ctx.children[0].getText()
        expr = self.pop()
        self.f.write('{}.add_reward("{}", {})\n'.format(self.ctmc, s, expr))

    def exitMarkovInitStateDecrelation(self, ctx:SHARPEParser.MarkovInitStateDecrelationContext):
        s = ctx.children[0].getText()
        expr = self.pop()
        self.f.write('{}.add_init("{}", {})\n'.format(self.ctmc, s, expr))

    def enterFtreeBlock(self, ctx:SHARPEParser.FtreeBlockContext):
        pass

    def exitFtreeBlock(self, ctx:SHARPEParser.FtreeBlockContext):
        pass

    def exitFtreeBlockDecleration(self, ctx:SHARPEParser.FtreeBlockDeclerationContext):
        x = ctx.children[1].getText()
        self.ft = x

    def exitFtreeRepeatDecrelation(self, ctx:SHARPEParser.FtreeRepeatDecrelationContext):
        x = ctx.children[1].getText()
        expr = self.pop()
        self.f.write('{} = relpy.FTEvent({})\n'.format(x, expr))

    def exitFtreeBasicDecrelation(self, ctx:SHARPEParser.FtreeBasicDecrelationContext):
        x = ctx.children[1].getText()
        expr = self.pop()
        self.f.write('{} = relpy.FTEvent({})\n'.format(x, expr))

    def exitFtreeAndDecrelation(self, ctx:SHARPEParser.FtreeAndDecrelationContext):
        x = ctx.children[1].getText()
        node = [ ctx.children[i].getText() for i in range(2,len(ctx.children))]
        self.f.write('{} = {}\n'.format(x, '&'.join(node)))

    def exitFtreeOrDecrelation(self, ctx:SHARPEParser.FtreeOrDecrelationContext):
        x = ctx.children[1].getText()
        node = [ ctx.children[i].getText() for i in range(2,len(ctx.children))]
        self.f.write('{} = {}\n'.format(x, '|'.join(node)))

    def exitFtreeKofNDecrelation(self, ctx:SHARPEParser.FtreeKofNDecrelationContext):
        x = ctx.children[1].getText()
        node = [ ctx.children[i].getText() for i in range(6,len(ctx.children))]
        n = self.pop()
        k = self.pop()
        self.f.write('{} = relpy.FTKofn({}.eval(), {}.eval(), [{}])\n'.format(x, k, n, ','.join(node)))

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

    def exitMarkovexrss_function(self, ctx:SHARPEParser.Markovexrss_functionContext):
        x = ctx.children[2]
        self.push('relpy.CTMCExrss({})'.format(x))

    def exitFtprob_function(self, ctx:SHARPEParser.Ftprob_functionContext):
        pass

    def exitFtsysprob_function(self, ctx:SHARPEParser.Ftsysprob_functionContext):
        x = ctx.children[2]
        self.push(x)
