from setuptools import setup, Extension
from Cython.Distutils import build_ext
import numpy
import os

catchmod = Extension('pycatchmod._catchmod', ['pycatchmod/_catchmod.pyx'],
                     include_dirs=[numpy.get_include()])
weather_generator = Extension('pycatchmod._weather_generator', ['pycatchmod/_weather_generator.pyx'],
                     include_dirs=[numpy.get_include()])

with open(os.path.join(os.path.dirname(__file__), "pycatchmod", "__init__.py"), "r") as f:
    for line in f:
        if line.startswith("__version__"):
            _, version, _ = line.split("\"")
            break

# needed to compile
setup_requires = [
    "cython", "numpy",
]
# needed to run
install_requires = [
    "numpy", "pandas", "click", "tables", "xlrd"
]
# only needed for testing
test_requires = [
    "pytest"
]

setup(
    name='pycatchmod',
    version=version,
    description='Python implementation of the rainfall runoff model CATCHMOD.',
    author='James E Tomlinson',
    author_email='tomo.bbe@gmail.com',
    packages=['pycatchmod', "pycatchmod.io"],
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=test_requires,
    ext_modules=[catchmod, weather_generator],
    cmdclass = {'build_ext': build_ext},
    entry_points={
        "console_scripts": [
            "pycatchmod = pycatchmod.__main__:main"
        ]
    }
)
