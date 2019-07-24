import relpy
env = relpy.Env()
b_os = relpy.Parameter("b_os")
rou_a = relpy.Parameter("rou_a")
delta_m = relpy.Parameter("delta_m")
pxy_rou_a = relpy.Parameter("pxy_rou_a")
rou_m = relpy.Parameter("rou_m")
mu_esw = relpy.Parameter("mu_esw")
phi = relpy.Parameter("phi")
mo_new = relpy.Parameter("mo_new")
mu_ps = relpy.Parameter("mu_ps")
pxy_rou_m = relpy.Parameter("pxy_rou_m")
n_i = relpy.Parameter("n_i")
delta_os = relpy.Parameter("delta_os")
plambda_esw = relpy.Parameter("plambda_esw")
pxy_beta_m = relpy.Parameter("pxy_beta_m")
mu_base = relpy.Parameter("mu_base")
n_o = relpy.Parameter("n_o")
mu_nic = relpy.Parameter("mu_nic")
pxy_delta1 = relpy.Parameter("pxy_delta1")
pxy_delta2 = relpy.Parameter("pxy_delta2")
plambda_c = relpy.Parameter("plambda_c")
mu_mp = relpy.Parameter("mu_mp")
plambda_nic = relpy.Parameter("plambda_nic")
gamma_die = relpy.Parameter("gamma_die")
m_stable1 = relpy.Parameter("m_stable1")
m_stable2 = relpy.Parameter("m_stable2")
m_setup = relpy.Parameter("m_setup")
beta_m = relpy.Parameter("beta_m")
pxy_gamma_die = relpy.Parameter("pxy_gamma_die")
beta_os = relpy.Parameter("beta_os")
plambda_os = relpy.Parameter("plambda_os")
plambda_hd = relpy.Parameter("plambda_hd")
pxy_gamma_hang = relpy.Parameter("pxy_gamma_hang")
mu_c = relpy.Parameter("mu_c")
delta1 = relpy.Parameter("delta1")
delta2 = relpy.Parameter("delta2")
plambda = relpy.Parameter("plambda")
mu_mem = relpy.Parameter("mu_mem")
mu_2c = relpy.Parameter("mu_2c")
t_setup = relpy.Parameter("t_setup")
plambda_base = relpy.Parameter("plambda_base")
plambda_mem = relpy.Parameter("plambda_mem")
mu_2hd = relpy.Parameter("mu_2hd")
pxy_delta_m = relpy.Parameter("pxy_delta_m")
gamma_hang = relpy.Parameter("gamma_hang")
pxy_phi = relpy.Parameter("pxy_phi")
pxy_mu = relpy.Parameter("pxy_mu")
plambda_ps = relpy.Parameter("plambda_ps")
chi_hd = relpy.Parameter("chi_hd")
rw_i = relpy.Parameter("rw_i")
mu_cpu = relpy.Parameter("mu_cpu")
b = relpy.Parameter("b")
c = relpy.Parameter("c")
rw_o = relpy.Parameter("rw_o")
d = relpy.Parameter("d")
e = relpy.Parameter("e")
c_ps = relpy.Parameter("c_ps")
pxy_b = relpy.Parameter("pxy_b")
pxy_c = relpy.Parameter("pxy_c")
plambda_cpu = relpy.Parameter("plambda_cpu")
mu_2ps = relpy.Parameter("mu_2ps")
pxy_d = relpy.Parameter("pxy_d")
pxy_e = relpy.Parameter("pxy_e")
t_stable1 = relpy.Parameter("t_stable1")
t_stable2 = relpy.Parameter("t_stable2")
mu_os = relpy.Parameter("mu_os")
q = relpy.Parameter("q")
alpha_sp = relpy.Parameter("alpha_sp")
mi_new = relpy.Parameter("mi_new")
r = relpy.Parameter("r")
mu_hd = relpy.Parameter("mu_hd")
plambda_mp = relpy.Parameter("plambda_mp")
mu = relpy.Parameter("mu")
pxy_q = relpy.Parameter("pxy_q")
pxy_r = relpy.Parameter("pxy_r")
c_mp = relpy.Parameter("c_mp")
env[b_os] = 0.95
env[rou_a] = 41.0390478956483
env[delta_m] = 2
env[pxy_rou_a] = 76.1791903844933
env[rou_m] = 10.9849424929091
env[mu_esw] = 2
env[phi] = 1241.37931034483
env[mo_new] = 3
env[mu_ps] = 2
env[pxy_rou_m] = 12.5323316751202
env[n_i] = 3
env[delta_os] = 2
env[plambda_esw] = 4.07871429136622e-007
env[pxy_beta_m] = 5.38628248508112
env[mu_base] = 2
env[n_o] = 4
env[mu_nic] = 2
env[pxy_delta1] = 3600
env[pxy_delta2] = 5.24781341107872
env[plambda_c] = 2.0547943798086e-007
env[mu_mp] = 2
env[plambda_nic] = 6.43835819290738e-007
env[gamma_die] = 0.000342465753424658
env[m_stable1] = 4
env[m_stable2] = 4
env[m_setup] = 4
env[beta_m] = 5.40946656649136
env[pxy_gamma_die] = 0.000342465753424658
env[beta_os] = 6
env[plambda_os] = 0.000114155251141553
env[plambda_hd] = 1.2214605736956e-006
env[pxy_gamma_hang] = 0.000342465753424658
env[mu_c] = 2
env[delta1] = 356.282784139751
env[delta2] = 5.24781341107872
env[plambda] = 100
env[mu_mem] = 2
env[mu_2c] = 1.71428571428571
env[t_setup] = 0.00416666666666667
env[plambda_base] = 3.49314470351934e-006
env[plambda_mem] = 1.12442935210381e-006
env[mu_2hd] = 1.71428571428571
env[pxy_delta_m] = 2
env[gamma_hang] = 0.000342465753424658
env[pxy_phi] = 360
env[pxy_mu] = 0.25
env[plambda_ps] = 2.46575072246496e-006
env[chi_hd] = 12
env[rw_i] = 0.00111111111111111
env[mu_cpu] = 2
env[b] = 0.95
env[c] = 0.95
env[rw_o] = 0.00333333333333333
env[d] = 0.95
env[e] = 0.95
env[c_ps] = 0.99
env[pxy_b] = 0.95
env[pxy_c] = 0.95
env[plambda_cpu] = 8.10502162825022e-007
env[mu_2ps] = 1.71428571428571
env[pxy_d] = 0.95
env[pxy_e] = 0.95
env[t_stable1] = 0.0125
env[t_stable2] = 0.0166666666666667
env[mu_os] = 2
env[q] = 0.95
env[alpha_sp] = 0.4
env[mi_new] = 2
env[r] = 0.95
env[mu_hd] = 2
env[plambda_mp] = 1.60958799376124e-006
env[mu] = 0.25
env[pxy_q] = 0.95
env[pxy_r] = 0.95
env[c_mp] = 0.0036101083032491
def ctmc_pairup(b, beta_m, c, d, delta1, delta2, delta_m, e, gamma, mu, phi, q, r, rou_a, rou_m):
     pairup = relpy.CTMC("pairup")
     pairup.add_trans("2U", "UO", (relpy.Const(2) * gamma))
     pairup.add_trans("UO", "1D", (d * delta1))
     pairup.add_trans("UO", "2D", (e * delta2))
     pairup.add_trans("UO", "1N", ((relpy.Const(1) - d) * delta1))
     pairup.add_trans("1N", "2D", (e * delta2))
     pairup.add_trans("1N", "UN", ((relpy.Const(1) - e) * delta2))
     pairup.add_trans("UO", "2N", ((relpy.Const(1) - e) * delta2))
     pairup.add_trans("2N", "UN", ((relpy.Const(1) - d) * delta1))
     pairup.add_trans("2N", "1D2N", (d * delta1))
     pairup.add_trans("1D", "FS", (c * phi))
     pairup.add_trans("1D", "FN", ((relpy.Const(1) - c) * phi))
     pairup.add_trans("S", "UA", (e * delta2))
     pairup.add_trans("S", "UR", ((relpy.Const(1) - e) * delta2))
     pairup.add_trans("N", "UC", (e * delta2))
     pairup.add_trans("N", "US", ((relpy.Const(1) - e) * delta2))
     pairup.add_trans("2D", "1D2D", delta1)
     pairup.add_trans("1D2D", "UA", (c * phi))
     pairup.add_trans("1D2D", "UC", ((relpy.Const(1) - c) * phi))
     pairup.add_trans("UA", "UR", ((relpy.Const(1) - q) * rou_a))
     pairup.add_trans("UA", "2U", (q * rou_a))
     pairup.add_trans("UR", "2U", (r * rou_m))
     pairup.add_trans("UR", "UB", ((relpy.Const(1) - r) * rou_m))
     pairup.add_trans("UB", "2U", beta_m)
     pairup.add_trans("UC", "US", ((relpy.Const(1) - q) * rou_a))
     pairup.add_trans("UC", "2U", (q * rou_a))
     pairup.add_trans("US", "2U", (r * rou_m))
     pairup.add_trans("US", "UT", ((relpy.Const(1) - r) * rou_m))
     pairup.add_trans("UT", "2U", (b * beta_m))
     pairup.add_trans("UT", "RP", ((relpy.Const(1) - b) * beta_m))
     pairup.add_trans("RP", "2U", mu)
     pairup.add_trans("UN", "MD", delta_m)
     pairup.add_trans("MD", "1D2N", delta1)
     pairup.add_trans("1D2N", "UR", (c * phi))
     pairup.add_trans("1D2N", "US", ((relpy.Const(1) - c) * phi))
     pairup.add_init("2U", relpy.Const(1))
     return pairup

def ctmc_pxy_pairup(pxy_b, pxy_beta_m, pxy_c, pxy_d, pxy_delta1, pxy_delta2, pxy_delta_m, pxy_e, pxy_gamma, pxy_mu, pxy_phi, pxy_q, pxy_r, pxy_rou_a, pxy_rou_m):
     pxy_pairup = relpy.CTMC("pxy_pairup")
     pxy_pairup.add_trans("2U", "UO", (relpy.Const(2) * pxy_gamma))
     pxy_pairup.add_trans("UO", "1D", (pxy_d * pxy_delta1))
     pxy_pairup.add_trans("UO", "2D", (pxy_e * pxy_delta2))
     pxy_pairup.add_trans("UO", "1N", ((relpy.Const(1) - pxy_d) * pxy_delta1))
     pxy_pairup.add_trans("1N", "2D", (pxy_e * pxy_delta2))
     pxy_pairup.add_trans("1N", "UN", ((relpy.Const(1) - pxy_e) * pxy_delta2))
     pxy_pairup.add_trans("UO", "2N", ((relpy.Const(1) - pxy_e) * pxy_delta2))
     pxy_pairup.add_trans("2N", "UN", ((relpy.Const(1) - pxy_d) * pxy_delta1))
     pxy_pairup.add_trans("2N", "1D2N", (pxy_d * pxy_delta1))
     pxy_pairup.add_trans("1D", "SO", (pxy_c * pxy_phi))
     pxy_pairup.add_trans("1D", "SN", ((relpy.Const(1) - pxy_c) * pxy_phi))
     pxy_pairup.add_trans("SO", "UA", (pxy_e * pxy_delta2))
     pxy_pairup.add_trans("SO", "UR", ((relpy.Const(1) - pxy_e) * pxy_delta2))
     pxy_pairup.add_trans("SN", "UC", (pxy_e * pxy_delta2))
     pxy_pairup.add_trans("SN", "US", ((relpy.Const(1) - pxy_e) * pxy_delta2))
     pxy_pairup.add_trans("2D", "1D2D", pxy_delta1)
     pxy_pairup.add_trans("1D2D", "UA", (pxy_c * pxy_phi))
     pxy_pairup.add_trans("1D2D", "UC", ((relpy.Const(1) - pxy_c) * pxy_phi))
     pxy_pairup.add_trans("UA", "UR", ((relpy.Const(1) - pxy_q) * pxy_rou_a))
     pxy_pairup.add_trans("UA", "2U", (pxy_q * pxy_rou_a))
     pxy_pairup.add_trans("UR", "2U", (pxy_r * pxy_rou_m))
     pxy_pairup.add_trans("UR", "UB", ((relpy.Const(1) - pxy_r) * pxy_rou_m))
     pxy_pairup.add_trans("UB", "2U", pxy_beta_m)
     pxy_pairup.add_trans("UC", "US", ((relpy.Const(1) - pxy_q) * pxy_rou_a))
     pxy_pairup.add_trans("UC", "2U", (pxy_q * pxy_rou_a))
     pxy_pairup.add_trans("US", "2U", (pxy_r * pxy_rou_m))
     pxy_pairup.add_trans("US", "UT", ((relpy.Const(1) - pxy_r) * pxy_rou_m))
     pxy_pairup.add_trans("UT", "2U", (pxy_b * pxy_beta_m))
     pxy_pairup.add_trans("UT", "RP", ((relpy.Const(1) - pxy_b) * pxy_beta_m))
     pxy_pairup.add_trans("RP", "2U", pxy_mu)
     pxy_pairup.add_trans("UN", "MD", pxy_delta_m)
     pxy_pairup.add_trans("MD", "1D2N", pxy_delta1)
     pxy_pairup.add_trans("1D2N", "UR", (pxy_c * pxy_phi))
     pxy_pairup.add_trans("1D2N", "US", ((relpy.Const(1) - pxy_c) * pxy_phi))
     pxy_pairup.add_init("2U", relpy.Const(1))
     return pxy_pairup

def ctmc_appserver(b, beta_m, d, delta1, delta2, delta_m, e, gamma, mu, q, r, rou_a, rou_m):
     appserver = relpy.CTMC("appserver")
     appserver.add_trans("UP", "UO", gamma)
     appserver.add_trans("UO", "UA", (e * delta2))
     appserver.add_trans("UO", "1D", (d * delta1))
     appserver.add_trans("UO", "1N", ((relpy.Const(1) - d) * delta1))
     appserver.add_trans("UO", "2N", ((relpy.Const(1) - e) * delta2))
     appserver.add_trans("1N", "UA", (e * delta2))
     appserver.add_trans("1N", "UN", ((relpy.Const(1) - e) * delta2))
     appserver.add_trans("2N", "UR", (d * delta1))
     appserver.add_trans("2N", "UN", ((relpy.Const(1) - d) * delta1))
     appserver.add_trans("1D", "UA", (e * delta2))
     appserver.add_trans("1D", "UR", ((relpy.Const(1) - e) * delta2))
     appserver.add_trans("UA", "UR", ((relpy.Const(1) - q) * rou_a))
     appserver.add_trans("UR", "UB", ((relpy.Const(1) - r) * rou_m))
     appserver.add_trans("UB", "RE", ((relpy.Const(1) - b) * beta_m))
     appserver.add_trans("UN", "UR", delta_m)
     appserver.add_trans("UA", "UP", (q * rou_a))
     appserver.add_trans("UR", "UP", (r * rou_m))
     appserver.add_trans("UB", "UP", (b * beta_m))
     appserver.add_trans("RE", "UP", mu)
     appserver.add_reward("UP", relpy.Const(1))
     return appserver

def ctmc_proxy(pxy_b, pxy_beta_m, pxy_d, pxy_delta1, pxy_delta2, pxy_delta_m, pxy_e, pxy_gamma, pxy_mu, pxy_q, pxy_r, pxy_rou_a, pxy_rou_m):
     proxy = relpy.CTMC("proxy")
     proxy.add_trans("UP", "UO", pxy_gamma)
     proxy.add_trans("UO", "UA", (pxy_e * pxy_delta2))
     proxy.add_trans("UO", "1N", ((relpy.Const(1) - pxy_d) * pxy_delta1))
     proxy.add_trans("UO", "2N", ((relpy.Const(1) - pxy_e) * pxy_delta2))
     proxy.add_trans("1N", "UA", (pxy_e * pxy_delta2))
     proxy.add_trans("1N", "UN", ((relpy.Const(1) - pxy_e) * pxy_delta2))
     proxy.add_trans("2N", "UR", (pxy_d * pxy_delta1))
     proxy.add_trans("2N", "UN", ((relpy.Const(1) - pxy_d) * pxy_delta1))
     proxy.add_trans("UA", "UR", ((relpy.Const(1) - pxy_q) * pxy_rou_a))
     proxy.add_trans("UR", "UB", ((relpy.Const(1) - pxy_r) * pxy_rou_m))
     proxy.add_trans("UB", "RE", ((relpy.Const(1) - pxy_b) * pxy_beta_m))
     proxy.add_trans("UO", "1D", (pxy_d * pxy_delta1))
     proxy.add_trans("1D", "UA", (pxy_e * pxy_delta2))
     proxy.add_trans("1D", "UR", ((relpy.Const(1) - pxy_e) * pxy_delta2))
     proxy.add_trans("UN", "UR", pxy_delta_m)
     proxy.add_trans("UA", "UP", (pxy_q * pxy_rou_a))
     proxy.add_trans("UR", "UP", (pxy_r * pxy_rou_m))
     proxy.add_trans("UB", "UP", (pxy_b * pxy_beta_m))
     proxy.add_trans("RE", "UP", pxy_mu)
     proxy.add_reward("UP", relpy.Const(1))
     return proxy

def ctmc_midplane(alpha_sp, c_mp, mu_mp, plambda_mp):
     midplane = relpy.CTMC("midplane")
     midplane.add_trans("UP", "DN", (c_mp * plambda_mp))
     midplane.add_trans("UP", "U1", ((relpy.Const(1) - c_mp) * plambda_mp))
     midplane.add_trans("U1", "RP", alpha_sp)
     midplane.add_trans("RP", "UP", mu_mp)
     midplane.add_trans("DN", "RP", alpha_sp)
     midplane.add_reward("UP", relpy.Const(1))
     midplane.add_reward("U1", relpy.Const(1))
     return midplane

def ctmc_cooling(alpha_sp, mu_2c, mu_c, plambda_c):
     cooling = relpy.CTMC("cooling")
     cooling.add_trans("UP", "U1", (relpy.Const(2) * plambda_c))
     cooling.add_trans("U1", "RP", alpha_sp)
     cooling.add_trans("U1", "DN", plambda_c)
     cooling.add_trans("DN", "DW", alpha_sp)
     cooling.add_trans("RP", "UP", mu_c)
     cooling.add_trans("RP", "DW", plambda_c)
     cooling.add_trans("DW", "UP", mu_2c)
     cooling.add_reward("UP", relpy.Const(1))
     cooling.add_reward("U1", relpy.Const(1))
     cooling.add_reward("RP", relpy.Const(1))
     return cooling

def ctmc_power(alpha_sp, c_ps, mu_2ps, mu_ps, plambda_ps):
     power = relpy.CTMC("power")
     power.add_trans("UP", "U1", ((relpy.Const(2) * c_ps) * plambda_ps))
     power.add_trans("UP", "DN", ((relpy.Const(2) * (relpy.Const(1) - c_ps)) * plambda_ps))
     power.add_trans("U1", "RP", alpha_sp)
     power.add_trans("U1", "DN", plambda_ps)
     power.add_trans("DN", "DW", alpha_sp)
     power.add_trans("RP", "UP", mu_ps)
     power.add_trans("RP", "DW", plambda_ps)
     power.add_trans("DW", "UP", mu_2ps)
     power.add_reward("UP", relpy.Const(1))
     power.add_reward("U1", relpy.Const(1))
     power.add_reward("RP", relpy.Const(1))
     return power

def ctmc_processor(alpha_sp, mu_cpu, plambda_cpu):
     processor = relpy.CTMC("processor")
     processor.add_trans("UP", "D1", (relpy.Const(2) * plambda_cpu))
     processor.add_trans("D1", "RP", alpha_sp)
     processor.add_trans("RP", "UP", mu_cpu)
     processor.add_reward("UP", relpy.Const(1))
     return processor

def ctmc_memory(alpha_sp, mu_mem, plambda_mem):
     memory = relpy.CTMC("memory")
     memory.add_trans("UP", "D1", (relpy.Const(4) * plambda_mem))
     memory.add_trans("D1", "RP", alpha_sp)
     memory.add_trans("RP", "UP", mu_mem)
     memory.add_reward("UP", relpy.Const(1))
     return memory

def ctmc_disk(alpha_sp, chi_hd, mu_2hd, mu_hd, plambda_hd):
     disk = relpy.CTMC("disk")
     disk.add_trans("UP", "U1", (relpy.Const(2) * plambda_hd))
     disk.add_trans("U1", "RP", alpha_sp)
     disk.add_trans("RP", "CP", mu_hd)
     disk.add_trans("CP", "DW", plambda_hd)
     disk.add_trans("U1", "DN", plambda_hd)
     disk.add_trans("DN", "DW", alpha_sp)
     disk.add_trans("CP", "UP", chi_hd)
     disk.add_trans("DW", "UP", mu_2hd)
     disk.add_reward("UP", relpy.Const(1))
     disk.add_reward("U1", relpy.Const(1))
     disk.add_reward("CP", relpy.Const(1))
     return disk

def ctmc_base(alpha_sp, mu_base, plambda_base):
     base = relpy.CTMC("base")
     base.add_trans("UP", "DN", plambda_base)
     base.add_trans("DN", "RP", alpha_sp)
     base.add_trans("RP", "UP", mu_base)
     base.add_reward("UP", relpy.Const(1))
     return base

def ctmc_OS(alpha_sp, b_os, beta_os, delta_os, mu_os, plambda_os):
     OS = relpy.CTMC("OS")
     OS.add_trans("UP", "DN", plambda_os)
     OS.add_trans("DN", "DT", delta_os)
     OS.add_trans("DT", "UP", (b_os * beta_os))
     OS.add_trans("DT", "DW", ((relpy.Const(1) - b_os) * beta_os))
     OS.add_trans("DW", "RP", alpha_sp)
     OS.add_trans("RP", "UP", mu_os)
     OS.add_reward("UP", relpy.Const(1))
     return OS

def ctmc_nic(alpha_sp, mu_nic, plambda_nic):
     nic = relpy.CTMC("nic")
     nic.add_trans("UP", "DN", plambda_nic)
     nic.add_trans("DN", "RP", alpha_sp)
     nic.add_trans("RP", "UP", mu_nic)
     nic.add_reward("UP", relpy.Const(1))
     return nic

def ctmc_switch(alpha_sp, mu_esw, plambda_esw):
     switch = relpy.CTMC("switch")
     switch.add_trans("UP", "DN", plambda_esw)
     switch.add_trans("DN", "RP", alpha_sp)
     switch.add_trans("RP", "UP", mu_esw)
     switch.add_reward("UP", relpy.Const(1))
     return switch

def bind_f_esw(plambda_esw, switch):
     return (relpy.CTMCStProb(switch,["UP"]) * plambda_esw)

def bind_f_nic(nic, plambda_nic):
     return (relpy.CTMCStProb(nic,["UP"]) * plambda_nic)

def bind_u_esw(f_esw, switch):
     return (f_esw / (relpy.Const(1) - relpy.CTMCExrss(switch)))

def bind_u_nic(f_nic, nic):
     return (f_nic / (relpy.Const(1) - relpy.CTMCExrss(nic)))

def ftree_network(_time, plambda_esw, plambda_nic):
     nic1 = relpy.FTEvent(env.bdd, relpy.ExpDist(plambda_nic, _time))
     nic2 = relpy.FTEvent(env.bdd, relpy.ExpDist(plambda_nic, _time))
     esw1 = relpy.FTEvent(env.bdd, relpy.ExpDist(plambda_esw, _time))
     esw2 = relpy.FTEvent(env.bdd, relpy.ExpDist(plambda_esw, _time))
     eth1 = relpy.FTOrGate([nic1,esw1])
     eth2 = relpy.FTOrGate([nic2,esw2])
     top = relpy.FTAndGate([eth1,eth2])
     return top

def ftree_CM(cooling, midplane, power):
     MP = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(midplane)))
     Cool = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(cooling)))
     Pwr = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(power)))
     top = relpy.FTOrGate([MP,Cool,Pwr])
     return top

def ftree_BLADE(OS, base, disk, memory, processor):
     Base = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(base)))
     CPU = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(processor)))
     Mem = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(memory)))
     RAID = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(disk)))
     OS = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(OS)))
     top = relpy.FTOrGate([Base,CPU,Mem,RAID,OS])
     return top

def ftree_CLUSTER(BLADE, CM, appserver, nic, proxy, switch):
     CM1 = relpy.FTEvent(env.bdd, CM)
     CM2 = relpy.FTEvent(env.bdd, CM)
     esw1 = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(switch)))
     esw2 = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(switch)))
     esw3 = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(switch)))
     esw4 = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(switch)))
     SW = relpy.FTBasicEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(appserver)))
     SWP = relpy.FTBasicEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(proxy)))
     Node_A = relpy.FTEvent(env.bdd, BLADE)
     nic1_A = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     nic2_A = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     eth1_A = relpy.FTOrGate([nic1_A,esw1])
     eth2_A = relpy.FTOrGate([nic2_A,esw2])
     eth_A = relpy.FTAndGate([eth1_A,eth2_A])
     BS_A = relpy.FTOrGate([Node_A,eth_A])
     Node_B = relpy.FTEvent(env.bdd, BLADE)
     nic1_B = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     nic2_B = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     eth1_B = relpy.FTOrGate([nic1_B,esw1])
     eth2_B = relpy.FTOrGate([nic2_B,esw2])
     eth_B = relpy.FTAndGate([eth1_B,eth2_B])
     BS_B = relpy.FTOrGate([Node_B,eth_B])
     Node_C = relpy.FTEvent(env.bdd, BLADE)
     nic1_C = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     nic2_C = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     eth1_C = relpy.FTOrGate([nic1_C,esw1])
     eth2_C = relpy.FTOrGate([nic2_C,esw2])
     eth_C = relpy.FTAndGate([eth1_C,eth2_C])
     BS_C = relpy.FTOrGate([Node_C,eth_C])
     Node_D = relpy.FTEvent(env.bdd, BLADE)
     nic1_D = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     nic2_D = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     eth1_D = relpy.FTOrGate([nic1_D,esw3])
     eth2_D = relpy.FTOrGate([nic2_D,esw4])
     eth_D = relpy.FTAndGate([eth1_D,eth2_D])
     BS_D = relpy.FTOrGate([Node_D,eth_D])
     Node_E = relpy.FTEvent(env.bdd, BLADE)
     nic1_E = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     nic2_E = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     eth1_E = relpy.FTOrGate([nic1_E,esw3])
     eth2_E = relpy.FTOrGate([nic2_E,esw4])
     eth_E = relpy.FTAndGate([eth1_E,eth2_E])
     BS_E = relpy.FTOrGate([Node_E,eth_E])
     Node_F = relpy.FTEvent(env.bdd, BLADE)
     nic1_F = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     nic2_F = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     eth1_F = relpy.FTOrGate([nic1_F,esw3])
     eth2_F = relpy.FTOrGate([nic2_F,esw4])
     eth_F = relpy.FTAndGate([eth1_F,eth2_F])
     BS_F = relpy.FTOrGate([Node_F,eth_F])
     Node_G = relpy.FTEvent(env.bdd, BLADE)
     nic1_G = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     nic2_G = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     eth1_G = relpy.FTOrGate([nic1_G,esw1])
     eth2_G = relpy.FTOrGate([nic2_G,esw2])
     eth_G = relpy.FTAndGate([eth1_G,eth2_G])
     BS_G = relpy.FTOrGate([Node_G,eth_G])
     Node_H = relpy.FTEvent(env.bdd, BLADE)
     nic1_H = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     nic2_H = relpy.FTEvent(env.bdd, (relpy.Const(1) - relpy.CTMCExrss(nic)))
     eth1_H = relpy.FTOrGate([nic1_H,esw3])
     eth2_H = relpy.FTOrGate([nic2_H,esw4])
     eth_H = relpy.FTAndGate([eth1_H,eth2_H])
     BS_H = relpy.FTOrGate([Node_H,eth_H])
     AS1 = relpy.FTOrGate([SW,BS_A,CM1])
     AS2 = relpy.FTOrGate([SW,BS_A,CM1])
     AS3 = relpy.FTOrGate([SW,BS_B,CM1])
     AS4 = relpy.FTOrGate([SW,BS_B,CM1])
     AS5 = relpy.FTOrGate([SW,BS_C,CM1])
     AS6 = relpy.FTOrGate([SW,BS_C,CM1])
     AS7 = relpy.FTOrGate([SW,BS_D,CM2])
     AS8 = relpy.FTOrGate([SW,BS_D,CM2])
     AS9 = relpy.FTOrGate([SW,BS_E,CM2])
     AS10 = relpy.FTOrGate([SW,BS_E,CM2])
     AS11 = relpy.FTOrGate([SW,BS_F,CM2])
     AS12 = relpy.FTOrGate([SW,BS_F,CM2])
     apps = relpy.FTKofnGate(relpy.Const(6).eval(env), relpy.Const(12).eval(env), [AS1,AS2,AS3,AS4,AS5,AS6,AS7,AS8,AS9,AS10,AS11,AS12])
     PX1 = relpy.FTOrGate([SWP,BS_G,CM1])
     PX2 = relpy.FTOrGate([SWP,BS_H,CM2])
     pxys = relpy.FTAndGate([PX1,PX2])
     top = relpy.FTOrGate([apps,pxys])
     return top

# pairup = ctmc_pairup(b, beta_m, c, d, delta1, delta2, delta_m, e, gamma, mu, phi, q, r, rou_a, rou_m)
# pxy_pairup = ctmc_pxy_pairup(pxy_b, pxy_beta_m, pxy_c, pxy_d, pxy_delta1, pxy_delta2, pxy_delta_m, pxy_e, pxy_gamma, pxy_mu, pxy_phi, pxy_q, pxy_r, pxy_rou_a, pxy_rou_m)
# appserver = ctmc_appserver(b, beta_m, d, delta1, delta2, delta_m, e, gamma, mu, q, r, rou_a, rou_m)
# proxy = ctmc_proxy(pxy_b, pxy_beta_m, pxy_d, pxy_delta1, pxy_delta2, pxy_delta_m, pxy_e, pxy_gamma, pxy_mu, pxy_q, pxy_r, pxy_rou_a, pxy_rou_m)
# midplane = ctmc_midplane(alpha_sp, c_mp, mu_mp, plambda_mp)
# cooling = ctmc_cooling(alpha_sp, mu_2c, mu_c, plambda_c)
# power = ctmc_power(alpha_sp, c_ps, mu_2ps, mu_ps, plambda_ps)
# processor = ctmc_processor(alpha_sp, mu_cpu, plambda_cpu)
# memory = ctmc_memory(alpha_sp, mu_mem, plambda_mem)
# disk = ctmc_disk(alpha_sp, chi_hd, mu_2hd, mu_hd, plambda_hd)
# base = ctmc_base(alpha_sp, mu_base, plambda_base)
# OS = ctmc_OS(alpha_sp, b_os, beta_os, delta_os, mu_os, plambda_os)
# nic = ctmc_nic(alpha_sp, mu_nic, plambda_nic)
# switch = ctmc_switch(alpha_sp, mu_esw, plambda_esw)
# f_esw = bind_f_esw(plambda_esw, switch)
# f_nic = bind_f_nic(nic, plambda_nic)
# u_esw = bind_u_esw(f_esw, switch)
# u_nic = bind_u_nic(f_nic, nic)
# network = ftree_network(_time, plambda_esw, plambda_nic)
# CM = ftree_CM(cooling, midplane, power)
# BLADE = ftree_BLADE(OS, base, disk, memory, processor)
# CLUSTER = ftree_CLUSTER(BLADE, CM, appserver, nic, proxy, switch)
def bind_gamma(gamma_die, gamma_hang):
     return (gamma_hang + gamma_die)

def bind_pxy_gamma(pxy_gamma_die, pxy_gamma_hang):
     return (pxy_gamma_hang + pxy_gamma_die)

# gamma = bind_gamma(gamma_die, gamma_hang)
# pxy_gamma = bind_pxy_gamma(pxy_gamma_die, pxy_gamma_hang)
