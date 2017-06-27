from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name = 'PBH',
    ext_modules = cythonize('PBH.pyx'),
    include_dirs=[np.get_include()]
)