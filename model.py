import relpy
env = relpy.Env()
def ftree_Non_Computers(mSA,mPRS,_time,mIRS):
     IRS = relpy.FTEvent(relpy.ExpDist(mIRS, _time))
     I2of3 = relpy.FTKofn(relpy.Const(2).eval(env), relpy.Const(3).eval(env), [IRS,IRS,IRS])
     PRS = relpy.FTEvent(relpy.ExpDist(mPRS, _time))
     P2of3 = relpy.FTKofn(relpy.Const(2).eval(env), relpy.Const(3).eval(env), [PRS,PRS,PRS])
     SA = relpy.FTEvent(relpy.ExpDist(mSA, _time))
     S2of3 = relpy.FTKofn(relpy.Const(2).eval(env), relpy.Const(3).eval(env), [SA,SA,SA])
     TOP = I2of3|P2of3|S2of3
     return relpy.FTEvent(TOP)

def ftree_CRASH(mCS,_time,Non_Computers):
     CS = relpy.FTEvent(relpy.ExpDist(mCS, _time))
     C3of4 = relpy.FTKofn(relpy.Const(3).eval(env), relpy.Const(4).eval(env), [CS,CS,CS,CS])
     others = relpy.FTEvent(Non_Computers)
     TOP = C3of4|others
     return relpy.FTEvent(TOP)

mIRS = relpy.Parameter("mIRS")
mPRS = relpy.Parameter("mPRS")
mSA = relpy.Parameter("mSA")
mCS = relpy.Parameter("mCS")
env[mIRS] = .000015
env[mPRS] = .000019
env[mSA] = .000037
env[mCS] = .00048
