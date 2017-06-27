from PBH import *
from concurrent.futures import ProcessPoolExecutor

mt = 170.85
xi = 100
mt_keys = np.array([170.85 + i/100 for i in range(4)])
xi_keys = np.array([10*i for i in range(1, 4)])
mt_run = []
for mt in mt_keys:
    mt_run.append((mt, xi, 44, 1e-04)) # Precision = 10^(-4)
pool = ProcessPoolExecutor(max_workers=4)
results = list(pool.map(RCC_parallel, mt_run))