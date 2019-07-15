import functools
from relpy.expr import *

class FaultTree(Parameterizable):
  def __init__(self):
    super().__init__()

  def __add__(self, other):
    return FTEvent(Add(self, other))

  def __and__(self, other):
    return FTAndGate(self, other)

  def __or__(self, other):
    return FTOrGate(self, other)
  
  def __invert__(self):
    return FTNotGate(self)

class FTEvent(FaultTree):
  def __init__(self, value):
    super().__init__()
    self.union_paramset([value])
    self.value = value

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
  def __init__(self, rate, tparam):
    super().__init__()
    self.union_paramset([rate,tparam])
    self.exponent = -rate * tparam

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
    super().__init__()
    self.union_paramset([value])
    self.value = value

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
  def __init__(self, left, right):
    super().__init__()
    self.union_paramset([left, right])
    self.left = left
    self.right = right

  def __repr__(self):
    return '{}&{}'.format(self.left, self.right)

  def __str__(self):
    return '{}&{}'.format(self.left, self.right)

  def eval(self, env):
    if self in env.cache:
      return env.cache[self]
    x = self.left.eval(env)
    y = self.right.eval(env)
    value = x * y
    env.cache[self] = value
    return value

  def deriv(self, env, p):
    if (self,p) in env.cache:
      return env.cache[(self,p)]
    if self.has_param(p):
      x = self.left.eval(env)
      y = self.right.eval(env)
      dx = self.left.deriv(env, p)
      dy = self.right.deriv(env, p)
      value = dx*y + x*dy
      env.cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2):
    if (self,p1,p2) in env.cache:
      return env.cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      x = self.left.eval(env)
      y = self.right.eval(env)
      dx1 = self.left.deriv(env, p1)
      dx2 = self.left.deriv(env, p2)
      dy1 = self.right.deriv(env, p1)
      dy2 = self.right.deriv(env, p2)
      dx12 = self.left.deriv2(env, p1, p2)
      dy12 = self.right.deriv2(env, p1, p2)
      value = dx12*y + dx1*dy2 + dx2*dy1 + x*dy12
      env.cache[(self,p1,p2)] = value
      return value
    else:
     return 0

class FTOrGate(FaultTree):
  def __init__(self, left, right):
    super().__init__()
    self.union_paramset([left, right])
    self.left = left
    self.right = right

  def __repr__(self):
    return '({}|{})'.format(self.left, self.right)

  def __str__(self):
    return '({}|{})'.format(self.left, self.right)

  def eval(self, env):
    if self in env.cache:
      return env.cache[self]
    x = self.left.eval(env)
    y = self.right.eval(env)
    value = 1 - (1-x) * (1-y)
    env.cache[self] = value
    return value

  def deriv(self, env, p):
    if (self,p) in env.cache:
      return env.cache[(self,p)]
    if self.has_param(p):
      x = self.left.eval(env)
      y = self.right.eval(env)
      dx = self.left.deriv(env, p)
      dy = self.right.deriv(env, p)
      value = dx * (1-y) + (1-x) * dy
      env.cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2):
    if (self,p1,p2) in env.cache:
      return env.cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      x = self.left.eval(env)
      y = self.right.eval(env)
      dx1 = self.left.deriv(env, p1)
      dx2 = self.left.deriv(env, p2)
      dy1 = self.right.deriv(env, p1)
      dy2 = self.right.deriv(env, p2)
      dx12 = self.left.deriv2(env, p1, p2)
      dy12 = self.right.deriv2(env, p1, p2)
      value = dx12 * (1-y) - dx1 * dy2 - dx2 * dy1 + (1-y) * dy12
      env.cache[(self,p1,p2)] = value
      return value
    else:
     return 0

class FTKofn(FaultTree):
  def __init__(self, k, n, nodes):
    super().__init__()
    self.k = k
    self.n = n
    if isinstance(nodes, list):
      self.union_paramset(nodes)
      self.nodes = nodes
    else:
      self.union_paramset([nodes])
      self.nodes = [nodes for i in range(n)]
    if self.k == 1:
      self.formula = functools.reduce(lambda a, b: a|b, self.nodes)
    elif self.k == self.n:
      self.formula = functools.reduce(lambda a, b: a&b, self.nodes)
    else:
      x = self.nodes[0]
      rnodes = self.nodes[1:]
      self.formula = (x & FTKofn(self.k-1, self.n-1, rnodes)) + ((~x) & FTKofn(self.k, self.n-1, rnodes))

  def __repr__(self):
    return 'KofN({},{}){}'.format(self.k, self.n, self.nodes)

  def __str__(self):
    return 'KofN({},{}){}'.format(self.k, self.n, self.nodes)

  def eval(self, env):
    if self in env.cache:
      return env.cache[self]
    x = self.formula.eval(env)
    value = x
    env.cache[self] = value
    return value

  def deriv(self, env, p):
    if (self,p) in env.cache:
      return env.cache[(self,p)]
    if self.has_param(p):
      dx = self.formula.deriv(env, p)
      value = dx
      env.cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2):
    if (self,p1,p2) in env.cache:
      return env.cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      dx12 = self.formula.deriv2(env, p1, p2)
      value = dx12
      env.cache[(self,p1,p2)] = value
      return value
    else:
     return 0

# functions

def ftprob(expr):
  return FTEvent(expr)
