from PBH import *
from concurrent.futures import ProcessPoolExecutor
import numpy as np
import pylab as plt
import seaborn as sns

mt = 170.88
xi = 100
mt_keys = np.array([170.8 + i/100 for i in range(10)])
xi_keys = np.array([10*i for i in range(1, 10)])

mt_read = []
for mt in mt_keys:
    mt_read.append((mt, xi))
pool = ProcessPoolExecutor(max_worker=8)
results_read = list(pool.map(Reader_parallel, mt_read))

for mt, Tup in zip(mt_keys, results_read):
    locals()['lH_'+str(mt)+'_'+str(xi)] = Tup[0]
    locals()['g1_'+str(mt)+'_'+str(xi)] = Tup[1]
    locals()['g2_'+str(mt)+'_'+str(xi)] = Tup[2]
    locals()['g3_'+str(mt)+'_'+str(xi)] = Tup[3]
    locals()['yt_'+str(mt)+'_'+str(xi)] = Tup[4]
    locals()['t_'+str(mt)+'_'+str(xi)] = Tup[5]
    locals()['phi_'+str(mt)+'_'+str(xi)] = Tup[6]
    locals()['G_'+str(mt)+'_'+str(xi)] = Tup[7]
    locals()['BlH_'+str(mt)+'_'+str(xi)] = Tup[8]
    locals()['V_'+str(mt)+'_'+str(xi)] = Pot_eff(xi, Tup)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.figure(figsize=(10,6), dpi=300)
for mt in mt_keys:
    for xi in xi_keys:
        plt.plot(locals()['t_'+str(mt)+'_'+str(xi)], locals()['lH_'+str(mt)+'_'+str(xi)], label=r'$M_t='+str(mt)+'$')
plt.title(r'$\xi='+str(xi)+'$', fontsize=16)
plt.xlabel(r'$t=\log(\mu/M_t)$', fontsize=14)
plt.ylabel(r'$\lambda$', fontsize=14)
plt.axis([32, 38, 0.0000, 0.0007])
plt.legend(fontsize=12)
plt.savefig("../PBH_Fig/lH_Mt_170_8_.png")

plt.figure(figsize=(10,6), dpi=300)
plt.plot(locals()['t_'+str(mt)+'_'+str(xi)], locals()['g1_'+str(mt)+'_'+str(xi)], label=r'$g_1$')
plt.plot(locals()['t_'+str(mt)+'_'+str(xi)], locals()['g2_'+str(mt)+'_'+str(xi)], label=r'$g_2$')
plt.plot(locals()['t_'+str(mt)+'_'+str(xi)], locals()['g3_'+str(mt)+'_'+str(xi)], label=r'$g_3$')
plt.plot(locals()['t_'+str(mt)+'_'+str(xi)], locals()['yt_'+str(mt)+'_'+str(xi)], label=r'$y_t$')
plt.title(r'$M_t =170.89GeV,\,\xi='+str(xi)+'$', fontsize=16)
plt.xlabel(r'$t=\log(\mu/M_t)$', fontsize=14)
plt.ylabel(r'Gauge Couplings', fontsize=14)
plt.legend(fontsize=14)
plt.savefig("../PBH_Fig/ga_Mt_170_88.png")

plt.figure(figsize=(10,6), dpi=300)
plt.plot(locals()['t_'+str(mt)+'_'+str(xi)], locals()['G_'+str(mt)+'_'+str(xi)], label=r'$M_t='+str(mt)+'$')
plt.title(r'$\xi='+str(xi)+'$', fontsize=16)
plt.xlabel(r'$t=\ln(\mu/M_t)$', fontsize=14)
plt.ylabel(r'$G(t)$', fontsize=14)
plt.legend(fontsize=12)
#plt.axis([0,2.4, 0, 2.5*10**(-8)])
plt.savefig("../PBH_Fig/G_Mt_170_88.png")

for mt in mt_keys:
    for xi in xi_keys:
        locals()['Rphi_'+str(mt)+'_'+str(xi)] = Normalize(locals()['phi_'+str(mt)+'_'+str(xi)],1)
        locals()['RV_'+str(mt)+'_'+str(xi)] = Normalize(locals()['V_'+str(mt)+'_'+str(xi)],4)

plt.figure(figsize=(10,6), dpi=300)
for mt in mt_keys:
    plt.plot(locals()['Rphi_'+str(mt)+'_'+str(xi)], locals()['RV_'+str(mt)+'_'+str(xi)], label=r'$M_t='+str(mt)+'$')
plt.title(r'$\xi='+str(xi)+'$', fontsize=16)
plt.xlabel(r'$\phi$ (in units of $M_p$)', fontsize=14)
plt.ylabel(r'$V_{eff}$ (in units of $M_p^4$)', fontsize=14)
plt.legend(fontsize=12)
plt.axis([0,25, -1*10**(-7), 1*10**(-6)])
plt.savefig("../PBH_Fig/V_Mt_170_8_.png")