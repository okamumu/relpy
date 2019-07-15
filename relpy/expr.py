import math

def exp(x):
  return Exp(x)

class Parameterizable:
  def __init__(self):
    self.paramset = set()

  def union_paramset(self, compo):
    for x in compo:
      self.paramset = self.paramset.union(x.get_paramset())
  
  def get_paramset(self):
    return self.paramset
  
  def set_paramset(self, paramset):
    self.paramset = paramset
  
  def has_param(self, param):
    return param in self.paramset
  
  def teval(self, tparam, t, env):
    env[tparam] = t
    return self.eval(env)

  def tderiv(self, tparam, t, env, p):
    env[tparam] = t
    return self.deriv(env, p)

  def tderiv2(self, tparam, t, env, p1, p2):
    env[tparam] = t
    return self.deriv2(env, p1, p2)

class Expr(Parameterizable):
  def __init__(self):
    super().__init__()

  def __add__(self, other):
    return Add(self, other)
  
  def __sub__(self, other):
    return Sub(self, other)
  
  def __mul__(self, other):
    return Mul(self, other)

  def __truediv__(self, other):
    return Div(self, other)

  def __pos__(self):
    return self

  def __neg__(self):
    return Neg(self)

class Parameter(Expr):
  def __init__(self, label):
    super().__init__()
    self.label = label
    s = set()
    s.add(self)
    self.set_paramset(s)

  def __repr__(self):
    return self.label

  def __str__(self):
    return self.label

  def eval(self, env):
    return env[self]

  def deriv(self, env, p):
    if self.has_param(p):
      return 1
    else:
      return 0

  def deriv2(self, env, p1, p2):
      return 0

class Const(Expr):
  def __init__(self, value):
    super().__init__()
    self.value = value
  
  def __repr__(self):
    return str(self.value)

  def __str__(self):
    return str(self.value)

  def eval(self):
    return self.value

  def eval(self, env):
    return self.value

  def deriv(self, env, p):
    return 0

  def deriv2(self, env, p1, p2):
    return 0

class Neg(Expr):
  def __init__(self, value):
    super().__init__()
    self.union_paramset([value])
    self.value = value

  def __repr__(self):
    return '(-{})'.format(self.value)

  def __str__(self):
    return '(-{})'.format(self.value)

  def eval(self, env):
    x = self.value.eval(env)
    return -x

  def deriv(self, env, p):
    if self.has_param(p):
      dx = self.value.deriv(env, p)
      return -dx
    else:
      return 0

  def deriv2(self, env, p1, p2):
    if self.has_param(p1) and self.has_param(p2):
      dx12 = self.value.deriv2(env, p1, p2)
      return -dx12
    else:
      return 0

class Add(Expr):
  def __init__(self, left, right):
    super().__init__()
    self.union_paramset([left, right])
    self.left = left
    self.right = right

  def __repr__(self):
    return '({}+{})'.format(self.left, self.right)

  def __str__(self):
    return '({}+{})'.format(self.left, self.right)

  def eval(self, env):
    if self in env.cache:
      return env.cache[self]
    x = self.left.eval(env)
    y = self.right.eval(env)
    value = x + y
    env.cache[self] = value
    return value

  def deriv(self, env, p):
    if (self,p) in env.cache:
      return env.cache[(self,p)]
    if self.has_param(p):
      dx = self.left.deriv(env, p)
      dy = self.right.deriv(env, p)
      value = dx + dy
      env.cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2):
    if (self,p1,p2) in env.cache:
      return env.cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      dx12 = self.left.deriv2(env, p1, p2)
      dy12 = self.right.deriv2(env, p1, p2)
      value = dx12 + dy12
      env.cache[(self,p1,p2)] = value
      return value
    else:
     return 0

class Sub(Expr):
  def __init__(self, left, right):
    super().__init__()
    self.union_paramset([left, right])
    self.left = left
    self.right = right

  def __repr__(self):
    return '({}-{})'.format(self.left, self.right)

  def __str__(self):
    return '({}-{})'.format(self.left, self.right)

  def eval(self, env):
    if self in env.cache:
      return env.cache[self]
    x = self.left.eval(env)
    y = self.right.eval(env)
    value = x - y
    env.cache[self] = value
    return value

  def deriv(self, env, p):
    if (self,p) in env.cache:
      return env.cache[(self,p)]
    if self.has_param(p):
      dx = self.left.deriv(env, p)
      dy = self.right.deriv(env, p)
      value = dx - dy
      env.cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2):
    if (self,p1,p2) in env.cache:
      return env.cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      dx12 = self.left.deriv2(env, p1, p2)
      dy12 = self.right.deriv2(env, p1, p2)
      value = dx12 - dy12
      env.cache[(self,p1,p2)] = value
      return value
    else:
     return 0

class Mul(Expr):
  def __init__(self, left, right):
    super().__init__()
    self.union_paramset([left, right])
    self.left = left
    self.right = right

  def __repr__(self):
    return '{}*{}'.format(self.left, self.right)

  def __str__(self):
    return '{}*{}'.format(self.left, self.right)

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

class Div(Expr):
  def __init__(self, left, right):
    super().__init__()
    self.union_paramset([left, right])
    self.left = left
    self.right = right

  def __repr__(self):
    return '{}/{}'.format(self.left, self.right)

  def __str__(self):
    return '{}/{}'.format(self.left, self.right)

  def eval(self, env):
    if self in env.cache:
      return env.cache[self]
    x = self.left.eval(env)
    y = self.right.eval(env)
    value = x / y
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
      value = (dx*y-x*dy)/y**2
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
      value = ((dx12*y + dx1*dy2 - dx2*dy1 - x*dy12) * y**2 - (dx1*y - x*dy1) * 2 * y * dy2) / y**4
      env.cache[(self,p1,p2)] = value
      return value
    else:
     return 0

class Exp(Expr):
  def __init__(self, exponent):
    super().__init__()
    self.union_paramset([exponent])
    self.exponent = exponent

  def __repr__(self):
    return 'exp({})'.format(self.exponent)

  def __str__(self):
    return 'exp({})'.format(self.exponent)

  def eval(self, env):
    if self in env.cache:
      return env.cache[self]
    x = self.exponent.eval(env)
    value = math.exp(x)
    env.cache[self] = value
    return value

  def deriv(self, env, p):
    if (self,p) in env.cache:
      return env.cache[(self,p)]
    if self.has_param(p):
      x = self.exponent.eval(env)
      dx = self.exponent.deriv(env, p)
      value = math.exp(x)*dx
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
      value = math.exp(x)*(dx1*dx2 + dx12)
      env.cache[(self,p1,p2)] = value
      return value
    else:
     return 0

