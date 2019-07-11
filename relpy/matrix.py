import numpy
import scipy.sparse
from relpy.expr import *

class Vector(Parameterizable):
  def __init__(self):
    super().__init__()
    self.states = set()
    self.elem = {}

  def __repr__(self):
    return 'Vector({})'.format(self.elem)

  def __str__(self):
    return 'Vector({})'.format(self.elem)

  def add(self, i, expr):
    self.union_paramset([expr])
    self.states.add(i)
    self.elem[i] = expr

  def eval(self, env, states = None):
    if states == None:
      states = self.states
    n = len(states)
    s = dict(zip(sorted(states), range(n)))
    x = numpy.zeros(n)
    for k,v in self.elem.items():
      x[s[k]] = v.eval(env)
    return x, s

  def deriv(self, env, p, states = None):
    if states == None:
      states = self.states
    n = len(states)
    s = dict(zip(sorted(states), range(n)))
    x = numpy.zeros(n)
    for k,v in self.elem.items():
      x[s[k]] = v.deriv(env, p)
    return x, s

  def deriv2(self, env, p1, p2, states = None):
    if states == None:
      states = self.states
    n = len(states)
    s = dict(zip(sorted(states), range(n)))
    x = numpy.zeros(n)
    for k,v in self.elem.items():
      x[s[k]] = v.deriv2(env, p1, p2)
    return x, s

class Matrix(Parameterizable):
  def __init__(self):
    super().__init__()
    self.row_states = set()
    self.col_states = set()
    self.elem = {}

  def __repr__(self):
    return 'Matrix({})'.format(self.elem)

  def __str__(self):
    return 'Matrix({})'.format(self.elem)

  def add(self, i, j, expr):
    self.union_paramset([expr])
    self.row_states.add(i)
    self.col_states.add(j)
    self.elem[(i,j)] = expr

  def make_matrix(self, shape, rowlist, collist, datalist):
    rowlist = [rowlist[i] for i in range(len(datalist)) if datalist[i] != 0.0]
    collist = [collist[i] for i in range(len(datalist)) if datalist[i] != 0.0]
    datalist = [datalist[i] for i in range(len(datalist)) if datalist[i] != 0.0]
    row = numpy.array(rowlist, dtype=numpy.int32)
    col = numpy.array(collist, dtype=numpy.int32)
    data = numpy.array(datalist, dtype=numpy.float64)
    return scipy.sparse.coo_matrix((data, (row, col)), shape=shape)

  def eval(self, env, row_states = None, col_states = None):
    if row_states == None:
      row_states = self.row_states
    if col_states == None:
      col_states = self.col_states
    m = len(row_states)
    n = len(col_states)
    si = dict(zip(sorted(row_states), range(m)))
    sj = dict(zip(sorted(col_states), range(n)))
    rowlist = [si[k[0]] for k in self.elem.keys()]
    collist = [sj[k[1]] for k in self.elem.keys()]
    datalist = [v.eval(env) for v in self.elem.values()]
    return self.make_matrix((m,n), rowlist, collist, datalist), si, sj

  def deriv(self, env, p, row_states = None, col_states = None):
    if row_states == None:
      row_states = self.row_states
    if col_states == None:
      col_states = self.col_states
    m = len(row_states)
    n = len(col_states)
    si = dict(zip(sorted(row_states), range(m)))
    sj = dict(zip(sorted(col_states), range(n)))
    rowlist = [si[k[0]] for k in self.elem.keys()]
    collist = [sj[k[1]] for k in self.elem.keys()]
    datalist = [v.deriv(env, p) for v in self.elem.values()]
    return self.make_matrix((m,n), rowlist, collist, datalist), si, sj

  def deriv2(self, env, p1, p2, row_states = None, col_states = None):
    if row_states == None:
      row_states = self.row_states
    if col_states == None:
      col_states = self.col_states
    m = len(row_states)
    n = len(col_states)
    si = dict(zip(sorted(row_states), range(m)))
    sj = dict(zip(sorted(col_states), range(n)))
    rowlist = [si[k[0]] for k in self.elem.keys()]
    collist = [sj[k[1]] for k in self.elem.keys()]
    datalist = [v.deriv2(env, p1, p2) for v in self.elem.values()]
    return self.make_matrix((m,n), rowlist, collist, datalist), si, sj

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

