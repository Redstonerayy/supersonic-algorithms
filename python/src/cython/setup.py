from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Optimized Quicksort',
    ext_modules=cythonize(["quicksort_full_optimization.pyx", "quicksort_with_types.pyx", "quicksort_no_optimization.pyx"]),
    include_dirs=["./lib/python3.10/site-packages/numpy/core/include"],
    zip_safe=False,
)
