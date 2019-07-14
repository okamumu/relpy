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

  def eval(self, env, cache):
    x = self.value.eval(env, cache)
    return x

  def deriv(self, env, p, cache):
    if self.has_param(p):
      dx = self.value.deriv(env, p, cache)
      return dx
    else:
     return 0

  def deriv2(self, env, p1, p2, cache):
    if self.has_param(p1) and self.has_param(p2):
      dx12 = self.value.deriv2(env, p1, p2, cache)
      return dx12
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

  def eval(self, env, cache):
    if self in cache:
      return cache[self]
    x = self.value.eval(env, cache)
    value = 1 - x
    cache[self] = value
    return value

  def deriv(self, env, p, cache):
    if (self,p) in cache:
      return cache[(self,p)]
    if self.has_param(p):
      dx = self.value.deriv(env, p, cache)
      value = -dx
      cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2, cache):
    if (self,p1,p2) in cache:
      return cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      dx12 = self.value.deriv2(env, p1, p2, cache)
      value = -dx12
      cache[(self,p1,p2)] = value
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

  def eval(self, env, cache):
    if self in cache:
      return cache[self]
    x = self.left.eval(env, cache)
    y = self.right.eval(env, cache)
    value = x * y
    cache[self] = value
    return value

  def deriv(self, env, p, cache):
    if (self,p) in cache:
      return cache[(self,p)]
    if self.has_param(p):
      x = self.left.eval(env, cache)
      y = self.right.eval(env, cache)
      dx = self.left.deriv(env, p, cache)
      dy = self.right.deriv(env, p, cache)
      value = dx*y + x*dy
      cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2, cache):
    if (self,p1,p2) in cache:
      return cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      x = self.left.eval(env, cache)
      y = self.right.eval(env, cache)
      dx1 = self.left.deriv(env, p1, cache)
      dx2 = self.left.deriv(env, p2, cache)
      dy1 = self.right.deriv(env, p1, cache)
      dy2 = self.right.deriv(env, p2, cache)
      dx12 = self.left.deriv2(env, p1, p2, cache)
      dy12 = self.right.deriv2(env, p1, p2, cache)
      value = dx12*y + dx1*dy2 + dx2*dy1 + x*dy12
      cache[(self,p1,p2)] = value
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

  def eval(self, env, cache):
    if self in cache:
      return cache[self]
    x = self.left.eval(env, cache)
    y = self.right.eval(env, cache)
    value = 1 - (1-x) * (1-y)
    cache[self] = value
    return value

  def deriv(self, env, p, cache):
    if (self,p) in cache:
      return cache[(self,p)]
    if self.has_param(p):
      x = self.left.eval(env, cache)
      y = self.right.eval(env, cache)
      dx = self.left.deriv(env, p, cache)
      dy = self.right.deriv(env, p, cache)
      value = dx * (1-y) + (1-x) * dy
      cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2, cache):
    if (self,p1,p2) in cache:
      return cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      x = self.left.eval(env, cache)
      y = self.right.eval(env, cache)
      dx1 = self.left.deriv(env, p1, cache)
      dx2 = self.left.deriv(env, p2, cache)
      dy1 = self.right.deriv(env, p1, cache)
      dy2 = self.right.deriv(env, p2, cache)
      dx12 = self.left.deriv2(env, p1, p2, cache)
      dy12 = self.right.deriv2(env, p1, p2, cache)
      value = dx12 * (1-y) - dx1 * dy2 - dx2 * dy1 + (1-y) * dy12
      cache[(self,p1,p2)] = value
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

  def eval(self, env, cache):
    if self in cache:
      return cache[self]
    x = self.formula.eval(env, cache)
    value = x
    cache[self] = value
    return value

  def deriv(self, env, p, cache):
    if (self,p) in cache:
      return cache[(self,p)]
    if self.has_param(p):
      dx = self.formula.deriv(env, p, cache)
      value = dx
      cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2, cache):
    if (self,p1,p2) in cache:
      return cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      dx12 = self.formula.deriv2(env, p1, p2, cache)
      value = dx12
      cache[(self,p1,p2)] = value
      return value
    else:
     return 0

# functions

def ftprob(expr):
  return FTEvent(expr)
