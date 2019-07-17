import functools
import relpy.bdd as bdd
from relpy.expr import *

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
    x = self.value.eval(env)
    return x

  def deriv(self, env, p):
    if self.has_param(p):
      dx = self.value.deriv(env, p)
      return dx
    else:
     return 0

  def deriv2(self, env, p1, p2):
    if self.has_param(p1) and self.has_param(p2):
      dx12 = self.value.deriv2(env, p1, p2)
      return dx12
    else:
     return 0

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

  def eval(self, env):
    if self in env.cache:
      return env.cache[self]
    x = self.exponent.eval(env)
    value = 1 - math.exp(x)
    env.cache[self] = value
    return value

  def deriv(self, env, p):
    if (self,p) in env.cache:
      return env.cache[(self,p)]
    if self.has_param(p):
      x = self.exponent.eval(env)
      dx = self.exponent.deriv(env, p)
      value = -math.exp(x)*dx
      env.cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2):
    if (self,p1,p2) in env.cache:
      return env.cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      x = self.exponent.eval(env)
      dx1 = self.exponent.deriv(env, p1)
      dx2 = self.exponent.deriv(env, p2)
      dx12 = self.exponent.deriv2(env, p1, p2)
      value = -math.exp(x)*(dx1*dx2 + dx12)
      env.cache[(self,p1,p2)] = value
      return value
    else:
     return 0

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

  def eval(self, env):
    if self in env.cache:
      return env.cache[self]
    x = self.value.eval(env)
    value = 1 - x
    env.cache[self] = value
    return value

  def deriv(self, env, p):
    if (self,p) in env.cache:
      return env.cache[(self,p)]
    if self.has_param(p):
      dx = self.value.deriv(env, p)
      value = -dx
      env.cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2):
    if (self,p1,p2) in env.cache:
      return env.cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      dx12 = self.value.deriv2(env, p1, p2)
      value = -dx12
      env.cache[(self,p1,p2)] = value
      return value
    else:
     return 0

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

  def eval(self, env):
    if self in env.cache:
      return env.cache[self]
    op = ProbOperator()
    value = op.comp(self, env, env.cache)
    env.cache[self] = value
    return value

  def deriv(self, env, p):
    pass
    # if (self,p) in env.cache:
    #   return env.cache[(self,p)]
    # if self.has_param(p):
    #   x = self.left.eval(env)
    #   y = self.right.eval(env)
    #   dx = self.left.deriv(env, p)
    #   dy = self.right.deriv(env, p)
    #   value = dx*y + x*dy
    #   env.cache[(self,p)] = value
    #   return value
    # else:
    #  return 0

  def deriv2(self, env, p1, p2):
    pass
    # if (self,p1,p2) in env.cache:
    #   return env.cache[(self,p1,p2)]
    # if self.has_param(p1) and self.has_param(p2):
    #   x = self.left.eval(env)
    #   y = self.right.eval(env)
    #   dx1 = self.left.deriv(env, p1)
    #   dx2 = self.left.deriv(env, p2)
    #   dy1 = self.right.deriv(env, p1)
    #   dy2 = self.right.deriv(env, p2)
    #   dx12 = self.left.deriv2(env, p1, p2)
    #   dy12 = self.right.deriv2(env, p1, p2)
    #   value = dx12*y + dx1*dy2 + dx2*dy1 + x*dy12
    #   env.cache[(self,p1,p2)] = value
    #   return value
    # else:
    #  return 0

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

  def eval(self, env):
    if self in env.cache:
      return env.cache[self]
    op = ProbOperator()
    value = op.comp(self, env, env.cache)
    env.cache[self] = value
    return value

  def deriv(self, env, p):
    pass
    # if (self,p) in env.cache:
    #   return env.cache[(self,p)]
    # if self.has_param(p):
    #   x = self.left.eval(env)
    #   y = self.right.eval(env)
    #   dx = self.left.deriv(env, p)
    #   dy = self.right.deriv(env, p)
    #   value = dx * (1-y) + (1-x) * dy
    #   env.cache[(self,p)] = value
    #   return value
    # else:
    #  return 0

  def deriv2(self, env, p1, p2):
    pass
    # if (self,p1,p2) in env.cache:
    #   return env.cache[(self,p1,p2)]
    # if self.has_param(p1) and self.has_param(p2):
    #   x = self.left.eval(env)
    #   y = self.right.eval(env)
    #   dx1 = self.left.deriv(env, p1)
    #   dx2 = self.left.deriv(env, p2)
    #   dy1 = self.right.deriv(env, p1)
    #   dy2 = self.right.deriv(env, p2)
    #   dx12 = self.left.deriv2(env, p1, p2)
    #   dy12 = self.right.deriv2(env, p1, p2)
    #   value = dx12 * (1-y) - dx1 * dy2 - dx2 * dy1 + (1-y) * dy12
    #   env.cache[(self,p1,p2)] = value
    #   return value
    # else:
    #  return 0

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

  def eval(self, env):
    if self in env.cache:
      return env.cache[self]
    op = ProbOperator()
    value = op.comp(self, env, env.cache)
    env.cache[self] = value
    return value

  def deriv(self, env, p):
    pass
    # if (self,p) in env.cache:
    #   return env.cache[(self,p)]
    # if self.has_param(p):
    #   dx = self.formula.deriv(env, p)
    #   value = dx
    #   env.cache[(self,p)] = value
    #   return value
    # else:
    #  return 0

  def deriv2(self, env, p1, p2):
    pass
    # if (self,p1,p2) in env.cache:
    #   return env.cache[(self,p1,p2)]
    # if self.has_param(p1) and self.has_param(p2):
    #   dx12 = self.formula.deriv2(env, p1, p2)
    #   value = dx12
    #   env.cache[(self,p1,p2)] = value
    #   return value
    # else:
    #  return 0

# functions

def ftprob(expr):
  return FTEvent(expr)

class ProbOperator(bdd.UnaryOperator):
  def comp(self, f, env, cache):
    self.env = env
    return self.apply(f.bdd, f.tree, cache)

  def applyT(self, bdd, f, cache):
    if f.value == True:
      return 1.0
    else:
      return 0.0

  def applyN(self, bdd, f, cache):
    p = f.var.eval(self.env)
    low = (1-p) * self.apply(bdd, f.low, cache)
    high = p * self.apply(bdd, f.high, cache)
    return low + high
