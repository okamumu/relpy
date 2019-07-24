import relpy
env = relpy.Env()
def ftree_Non_Computers(_time, mIRS, mPRS, mSA):
     IRS = relpy.FTBasicEvent(env.bdd, relpy.ExpDist(mIRS, _time))
     I2of3 = relpy.FTKofnGate(relpy.Const(2).eval(env), relpy.Const(3).eval(env), [IRS,IRS,IRS])
     PRS = relpy.FTBasicEvent(env.bdd, relpy.ExpDist(mPRS, _time))
     P2of3 = relpy.FTKofnGate(relpy.Const(2).eval(env), relpy.Const(3).eval(env), [PRS,PRS,PRS])
     SA = relpy.FTBasicEvent(env.bdd, relpy.ExpDist(mSA, _time))
     S2of3 = relpy.FTKofnGate(relpy.Const(2).eval(env), relpy.Const(3).eval(env), [SA,SA,SA])
     TOP = relpy.FTOrGate([I2of3,P2of3,S2of3])
     return TOP

def ftree_CRASH(Non_Computers, _time, mCS):
     CS = relpy.FTBasicEvent(env.bdd, relpy.ExpDist(mCS, _time))
     C3of4 = relpy.FTKofnGate(relpy.Const(3).eval(env), relpy.Const(4).eval(env), [CS,CS,CS,CS])
     others = relpy.FTBasicEvent(env.bdd, Non_Computers)
     TOP = relpy.FTOrGate([C3of4,others])
     return TOP

mIRS = relpy.Parameter("mIRS")
mPRS = relpy.Parameter("mPRS")
mSA = relpy.Parameter("mSA")
mCS = relpy.Parameter("mCS")
env[mIRS] = .000015
env[mPRS] = .000019
env[mSA] = .000037
env[mCS] = .00048
# Non_Computers = ftree_Non_Computers(_time, mIRS, mPRS, mSA)
# CRASH = ftree_CRASH(Non_Computers, _time, mCS)
