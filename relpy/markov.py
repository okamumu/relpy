from relpy.expr import *
from relpy.ftree import *
from relpy.matrix import *
from relpy.nmarkov import *
import numpy as np

class CTMCMatrix(Matrix):
  def __init__(self):
    super().__init__()

  def make_matrix(self, shape, rowlist, collist, datalist):
    collist += rowlist
    rowlist += rowlist
    datalist += [-x for x in datalist]
    rowlist = [rowlist[i] for i in range(len(datalist)) if datalist[i] != 0.0]
    collist = [collist[i] for i in range(len(datalist)) if datalist[i] != 0.0]
    datalist = [datalist[i] for i in range(len(datalist)) if datalist[i] != 0.0]
    row = numpy.array(rowlist, dtype=numpy.int32)
    col = numpy.array(collist, dtype=numpy.int32)
    data = numpy.array(datalist, dtype=numpy.float64)
    return scipy.sparse.coo_matrix((data, (row, col)), shape=shape)

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

  def getQ(self, env):
    Q = self.Q.eval(env, row_states=self.states, col_states=self.states)
    return Q

  def getQ_deriv(self, env, p):
    Q = self.Q.deriv(env, p, row_states=self.states, col_states=self.states)
    return Q

  def getQ_deriv2(self, env, p1, p2):
    Q = self.Q.deriv2(env, p1, p2, row_states=self.states, col_states=self.states)
    return Q

  def get_reward(self, env):
    r = self.reward.eval(env, states=self.states)
    return r

  def get_reward_deriv(self, env, p):
    r = self.reward.deriv(env, p, states=self.states)
    return r

  def get_reward_deriv2(self, env, p1, p2):
    r = self.reward.deriv2(env, p1, p2, states=self.states)
    return r

  def get_init(self, env):
    r = self.init.eval(env, states=self.states)
    return r

  def get_init_deriv(self, env, p):
    r = self.init.deriv(env, p, states=self.states)
    return r

  def get_init_deriv2(self, env, p1, p2):
    r = self.init.deriv2(env, p1, p2, states=self.states)
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

  def _eval(self, env):
    Q,si,sj = self.markov.getQ(env)
    pis = self.solve(Q)
    return sum([pis[si[k]] for k in self.states])

  def _deriv(self, env, p):
    Q,si,sj = self.markov.getQ(env)
    dQ,si,sj = self.markov.getQ_deriv(env, p)
    pis = self.solve(Q)
    dpis = self.sensolve(Q, pis * dQ, pis)
    return sum([dpis[si[k]] for k in self.states])

  def _deriv2(self, env, p1, p2):
    Q,si,sj = self.markov.getQ(env)
    dQ1,si,sj = self.markov.getQ_deriv(env, p1)
    dQ2,si,sj = self.markov.getQ_deriv(env, p2)
    dQ12,si,sj = self.markov.getQ_deriv2(env, p1, p2)
    pis = self.solve(Q)
    s1 = self.sensolve(Q, pis*dQ1, pis)
    s2 = self.sensolve(Q, pis*dQ2, pis)
    s12 = self.sensolve(Q, pis*dQ12 + s1*dQ2 + s2*dQ1, pis)
    return sum([s12[si[k]] for k in self.states])

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

  def _eval(self, env):
    Q,si,sj = self.markov.getQ(env)
    r,s = self.markov.get_reward(env)
    pis = self.solve(Q)
    return np.dot(pis, r)

  def _deriv(self, env, p):
    Q,si,sj = self.markov.getQ(env)
    dQ,si,sj = self.markov.getQ_deriv(env, p)
    r,s = self.markov.get_reward(env)
    dr,s = self.markov.get_reward_deriv(env, p)
    pis = self.solve(Q)
    dpis = self.sensolve(Q, pis*dQ, pis)
    return np.dot(dpis, r) + np.dot(pis, dr)

  def _deriv2(self, env, p1, p2):
    Q,si,sj = self.markov.getQ(env)
    dQ1,si,sj = self.markov.getQ_deriv(env, p1)
    dQ2,si,sj = self.markov.getQ_deriv(env, p2)
    dQ12,si,sj = self.markov.getQ_deriv2(env, p1, p2)
    r,s = self.markov.get_reward(env)
    dr1,s = self.markov.get_reward_deriv(env, p1)
    dr2,s = self.markov.get_reward_deriv(env, p2)
    dr12,s = self.markov.get_reward_deriv2(env, p1, p2)
    pis = self.solve(Q)
    s1 = self.sensolve(Q, pis*dQ1, pis)
    s2 = self.sensolve(Q, pis*dQ2, pis)
    s12 = self.sensolve(Q, pis*dQ12 + s1*dQ2 + s2*dQ1, pis)
    return np.dot(s12, r) + np.dot(s1, dr2) + np.dot(s2, dr1) + np.dot(pis, dr12)

### markov funcs

def marprob(m, s):
  return CTMCStProb(m, s)

def marexrss(m):
  return CTMCExrss(m)

