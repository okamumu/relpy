from relpy.expr import *
from relpy.ftree import *
from relpy.matrix import *
from relpy.nmarkov import *
import numpy as np

class CTMC(Parameterizable):
  def __init__(self, label):
    super().__init__()
    self.label = label
    self.states = set()
    self.Q = CTMCMatrix()
    self.init = Vector()
    self.reward = Vector()

  def set_label(self, label):
    self.label = label
    
  def __repr__(self):
    return self.label

  def __str__(self):
    return self.label

  def add_trans(self, s, d, expr):
    self.union_paramset([expr])
    self.states.add(s)
    self.states.add(d)
    self.Q.add(s, d, expr)
    
  def add_reward(self, s, expr):
    self.union_paramset([expr])
    self.states.add(s)
    self.reward.add(s, expr)

  def add_init(self, s, expr):
    self.union_paramset([expr])
    self.states.add(s)
    self.init.add(s, expr)

  def getQ(self, env, cache):
    Q = self.Q.eval(env, cache, row_states=self.states, col_states=self.states)
    return Q

  def getQ_deriv(self, env, p, cache):
    Q = self.Q.deriv(env, p, cache, row_states=self.states, col_states=self.states)
    return Q

  def getQ_deriv2(self, env, p1, p2, cache):
    Q = self.Q.deriv2(env, p1, p2, cache, row_states=self.states, col_states=self.states)
    return Q

  def get_reward(self, env, cache):
    r = self.reward.eval(env, cache, states=self.states)
    return r

  def get_reward_deriv(self, env, p, cache):
    r = self.reward.deriv(env, p, cache, states=self.states)
    return r

  def get_reward_deriv2(self, env, p1, p2, cache):
    r = self.reward.deriv2(env, p1, p2, cache, states=self.states)
    return r

  def get_init(self, env, cache):
    r = self.init.eval(env, cache, states=self.states)
    return r

  def get_init_deriv(self, env, p, cache):
    r = self.init.deriv(env, p, cache, states=self.states)
    return r

  def get_init_deriv2(self, env, p1, p2, cache):
    r = self.init.deriv2(env, p1, p2, cache, states=self.states)
    return r

class CTMCStProb(Expr):
  def __init__(self, markov, states):
    super().__init__()
    self.set_paramset(markov.Q.get_paramset())
    self.markov = markov
    self.states = states
    self.params = Params()
    self.nmax = 100

  def __repr__(self):
    return 'CTMCStProb({}, {})'.format(self.markov, self.states)

  def __str__(self):
    return 'CTMCStProb({}, {})'.format(self.markov, self.states)

  def solve(self, Q):
    Q = Q.tocsc()
    n = Q.shape[0]
    if n > self.nmax:
      x0 = np.full(n, 1/n)
      return ctmc_st_gs_sparse(Q, x0, self.params)
    else:
      return ctmc_st_gth_sparse(Q)

  def sensolve(self, Q, b, pis):
    Q = Q.tocsc()
    n = Q.shape[0]
    x0 = np.full(n, 0.0)
    return ctmc_stsen_gs_sparse(Q, x0, b, pis, self.params)

  def eval(self, env, cache):
    if self in cache:
      return cache[self]
    Q,si,sj = self.markov.getQ(env, cache)
    pis = self.solve(Q)
    value = sum([pis[si[k]] for k in self.states])
    cache[self] = value
    return value

  def deriv(self, env, p, cache):
    if (self,p) in cache:
      return cache[(self,p)]
    if self.has_param(p):
      Q,si,sj = self.markov.getQ(env, cache)
      dQ,si,sj = self.markov.getQ_deriv(env, p, cache)
      pis = self.solve(Q)
      dpis = self.sensolve(Q, pis * dQ, pis)
      value = sum([dpis[si[k]] for k in self.states])
      cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2, cache):
    if (self,p1,p2) in cache:
      return cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      Q,si,sj = self.markov.getQ(env, cache)
      dQ1,si,sj = self.markov.getQ_deriv(env, p1, cache)
      dQ2,si,sj = self.markov.getQ_deriv(env, p2, cache)
      dQ12,si,sj = self.markov.getQ_deriv2(env, p1, p2, cache)
      pis = self.solve(Q)
      s1 = self.sensolve(Q, pis*dQ1, pis)
      s2 = self.sensolve(Q, pis*dQ2, pis)
      s12 = self.sensolve(Q, pis*dQ12 + s1*dQ2 + s2*dQ1, pis)
      value = sum([s12[si[k]] for k in self.states])
      cache[(self,p1,p2)] = value
      return value
    else:
     return 0

class CTMCExrss(Expr):
  def __init__(self, markov):
    super().__init__()
    self.set_paramset(markov.Q.get_paramset().union(markov.reward.get_paramset()))
    self.markov = markov
    self.params = Params()
    self.nmax = 100

  def __repr__(self):
    return 'CTMCExrss({})'.format(self.markov)

  def __str__(self):
    return 'CTMCExrss({})'.format(self.markov)

  def solve(self, Q):
    Q = Q.tocsc()
    n = Q.shape[0]
    if n > self.nmax:
      x0 = np.full(n, 1/n)
      return ctmc_st_gs_sparse(Q, x0, self.params)
    else:
      return ctmc_st_gth_sparse(Q)

  def sensolve(self, Q, b, pis):
    Q = Q.tocsc()
    n = Q.shape[0]
    x0 = np.full(n, 0.0)
    return ctmc_stsen_gs_sparse(Q, x0, b, pis, self.params)

  def eval(self, env, cache):
    if self in cache:
      return cache[self]
    Q,si,sj = self.markov.getQ(env, cache)
    r,s = self.markov.get_reward(env, cache)
    pis = self.solve(Q)
    value = np.dot(pis, r)
    cache[self] = value
    return value

  def deriv(self, env, p, cache):
    if (self,p) in cache:
      return cache[(self,p)]
    if self.has_param(p):
      Q,si,sj = self.markov.getQ(env, cache)
      dQ,si,sj = self.markov.getQ_deriv(env, p, cache)
      r,s = self.markov.get_reward(env, cache)
      dr,s = self.markov.get_reward_deriv(env, p, cache)
      pis = self.solve(Q)
      dpis = self.sensolve(Q, pis*dQ, pis)
      value = np.dot(dpis, r) + np.dot(pis, dr)
      cache[(self,p)] = value
      return value
    else:
     return 0

  def deriv2(self, env, p1, p2, cache):
    if (self,p1,p2) in cache:
      return cache[(self,p1,p2)]
    if self.has_param(p1) and self.has_param(p2):
      Q,si,sj = self.markov.getQ(env, cache)
      dQ1,si,sj = self.markov.getQ_deriv(env, p1, cache)
      dQ2,si,sj = self.markov.getQ_deriv(env, p2, cache)
      dQ12,si,sj = self.markov.getQ_deriv2(env, p1, p2, cache)
      r,s = self.markov.get_reward(env, cache)
      dr1,s = self.markov.get_reward_deriv(env, p1, cache)
      dr2,s = self.markov.get_reward_deriv(env, p2, cache)
      dr12,s = self.markov.get_reward_deriv2(env, p1, p2, cache)
      pis = self.solve(Q)
      s1 = self.sensolve(Q, pis*dQ1, pis)
      s2 = self.sensolve(Q, pis*dQ2, pis)
      s12 = self.sensolve(Q, pis*dQ12 + s1*dQ2 + s2*dQ1, pis)
      value = np.dot(s12, r) + np.dot(s1, dr2) + np.dot(s2, dr1) + np.dot(pis, dr12)
      cache[(self,p1,p2)] = value
      return value
    else:
     return 0

### markov funcs

def marprob(m, s):
  return CTMCStProb(m, s)

def marexrss(m):
  return CTMCExrss(m)

