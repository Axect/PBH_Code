from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = 'PBH',
    ext_modules = cythonize('PBH.pyx')
)