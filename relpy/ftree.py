import functools
import relpy.bdd as bdd
from relpy.expr import *
import numpy as np

class FaultTree(Parameterizable):
  def __init__(self, bdd):
    super().__init__()
    self.bdd = bdd

  def __and__(self, other):
    return FTAndGate([self, other])

  def __or__(self, other):
    return FTOrGate([self, other])
  
  def __invert__(self):
    return FTNotGate(self)

class FTEvent(FaultTree):
  def __init__(self, bdd, value):
    super().__init__(bdd)
    self.union_paramset([value])
    self.value = value
    self.tree = bdd.var(self)

  def __repr__(self):
    return '{}'.format(self.value)

  def __str__(self):
    return '{}'.format(self.value)

  def eval(self, env):
    return self.value.eval(env)

  def deriv(self, env, p):
    return self.value.deriv(env, p)

  def deriv2(self, env, p1, p2):
    return self.value.deriv2(env, p1, p2)

class ExpDist(FaultTree):
  def __init__(self, bdd, rate, tparam):
    super().__init__(bdd)
    self.union_paramset([rate,tparam])
    self.exponent = -rate * tparam
    self.tree = bdd.var(self)

  def __repr__(self):
    return 'exp({})'.format(self.exponent)

  def __str__(self):
    return 'exp({})'.format(self.exponent)

  def _eval(self, env):
    x = self.exponent.eval(env)
    return 1 - math.exp(x)

  def _deriv(self, env, p):
    x = self.exponent.eval(env)
    dx = self.exponent.deriv(env, p)
    return -math.exp(x)*dx

  def _deriv2(self, env, p1, p2):
    x = self.exponent.eval(env)
    dx1 = self.exponent.deriv(env, p1)
    dx2 = self.exponent.deriv(env, p2)
    dx12 = self.exponent.deriv2(env, p1, p2)
    return -math.exp(x)*(dx1*dx2 + dx12)

class FTNotGate(FaultTree):
  def __init__(self, value):
    super().__init__(value.bdd)
    self.union_paramset([value])
    self.value = value
    self.tree = value.bdd.Not(value.tree)

  def __repr__(self):
    return '~{}'.format(self.value)

  def __str__(self):
    return '~{}'.format(self.value)

  def _eval(self, env):
    return 1-self.value.eval(env)

  def _deriv(self, env, p):
    return -self.value.deriv(env, p)

  def _deriv2(self, env, p1, p2):
    return -self.value.deriv2(env, p1, p2)

class FTAndGate(FaultTree):
  def __init__(self, nodes):
    super().__init__(nodes[0].bdd)
    self.union_paramset(nodes)
    self.value = nodes
    self.tree = bdd.createAndGate(nodes[0].bdd, [x.tree for x in nodes])

  def __repr__(self):
    return '({})'.format('&'.join([str(x) for x in self.value]))

  def __str__(self):
    return '({})'.format('&'.join([str(x) for x in self.value]))

  def _eval(self, env):
    op = EvalOperator()
    return op.comp(self, env)

  def _deriv(self, env, p):
    op = DerivOperator()
    return op.comp(self, env, p)

  def _deriv2(self, env, p1, p2):
    op = Deriv2Operator()
    return op.comp(self, env, p1, p2)

class FTOrGate(FaultTree):
  def __init__(self, nodes):
    super().__init__(nodes[0].bdd)
    self.union_paramset(nodes)
    self.value = nodes
    self.tree = bdd.createOrGate(nodes[0].bdd, [x.tree for x in nodes])

  def __repr__(self):
    return '({})'.format('|'.join([str(x) for x in self.value]))

  def __str__(self):
    return '({})'.format('|'.join([str(x) for x in self.value]))

  def _eval(self, env):
    op = EvalOperator()
    return op.comp(self, env)

  def _deriv(self, env, p):
    op = DerivOperator()
    return op.comp(self, env, p)

  def _deriv2(self, env, p1, p2):
    op = Deriv2Operator()
    return op.comp(self, env, p1, p2)

class FTKofnGate(FaultTree):
  def __init__(self, k, n, nodes):
    super().__init__(nodes[0].bdd)
    self.union_paramset(nodes)
    self.k = k
    self.n = n
    self.value = nodes
    self.tree = bdd.createKofNGate(nodes[0].bdd, k, n, [x.tree for x in nodes])

  def __repr__(self):
    return '{}of{}({})'.format(self.k, self.n, ','.join([str(x) for x in self.value]))

  def __str__(self):
    return '{}of{}({})'.format(self.k, self.n, ','.join([str(x) for x in self.value]))

  def _eval(self, env):
    op = EvalOperator()
    return op.comp(self, env)

  def _deriv(self, env, p):
    op = DerivOperator()
    return op.comp(self, env, p)

  def _deriv2(self, env, p1, p2):
    op = Deriv2Operator()
    return op.comp(self, env, p1, p2)

# functions

def ftprob(expr):
  return FTEvent(expr)

class EvalOperator:
  def comp(self, f, env):
    return self.apply(f.tree, env)

  def apply(self, f, env):
      if f in env.cache:
          return env.cache[f]
      if f.isValue() == True:
          result = self.applyT(f, env)
      else:
          result = self.applyN(f, env)
      env.cache[f] = result
      return result

  def applyT(self, f, env):
    if f.value == True:
      return 1.0
    else:
      return 0.0

  def applyN(self, f, env):
    p = f.var.eval(env)
    low = (1-p) * self.apply(f.low, env)
    high = p * self.apply(f.high, env)
    return low + high

class DerivOperator(EvalOperator):
  def comp(self, f, env, p):
    return self.dapply(f.tree, env, p)

  def dapply(self, f, env, p):
    if (f,p) in env.cache:
        return env.cache[(f,p)]
    if f.isValue() == True:
        result = self.dapplyT(f, env, p)
    else:
        result = self.dapplyN(f, env, p)
    env.cache[(f,p)] = result
    return result

  def dapplyT(self, f, env, p):
    return 0.0

  def dapplyN(self, f, env, p):
    x = f.var.eval(env)
    dx = f.var.deriv(env, p)
    low = -dx * self.apply(f.low, env) + (1-x) * self.dapply(f.low, env, p)
    high = dx * self.apply(f.high, env) + x * self.dapply(f.high, env, p)
    return low + high

class Deriv2Operator(DerivOperator):
  def comp(self, f, env, p1, p2):
    return self.ddapply(f.tree, env, p1, p2)

  def ddapply(self, f, env, p1, p2):
    if (f,p1,p2) in env.cache:
        return env.cache[(f,p1,p2)]
    if f.isValue() == True:
        result = self.ddapplyT(f, env, p1, p2)
    else:
        result = self.ddapplyN(f, env, p1, p2)
    env.cache[(f,p1,p2)] = result
    return result

  def ddapplyT(self, f, env, p1, p2):
    return 0.0

  def ddapplyN(self, f, env, p1, p2):
    x = f.var.eval(env)
    dx1 = f.var.deriv(env, p1)
    dx2 = f.var.deriv(env, p2)
    dx12 = f.var.deriv2(env, p1, p2)
    low = -dx12 * self.apply(f.low, env) - dx1 * self.dapply(f.low, env, p2) - dx2 * self.dapply(f.low, env, p1) + (1-x) * self.ddapply(f.low, env, p1, p2)
    high = dx12 * self.apply(f.high, env) + dx1 * self.dapply(f.high, env, p2) + dx2 * self.dapply(f.high, env, p1) + x * self.ddapply(f.high, env, p1, p2)
    return low + high
