from Cython.Build import cythonize
from setuptools.extension import Extension
from setuptools import setup, find_packages
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
include_dirs = [dir_path + "/src", dir_path]
macros = [("CYTHON_TRACE", "1")]
extensions = [Extension("quicksect", ["src/quicksect.pyx"],
                        define_macros=macros,
                        include_dirs=include_dirs)]

setup(version='0.2.2',
	  name='quicksect',
      description="fast, simple interval intersection",
      ext_modules = cythonize(extensions, language_level=3),
      long_description=open('README.rst').read(),
      author="Brent Pedersen,Jianlin Shi",
      author_email="bpederse@gmail.com, jianlinshi.cn@gmail.com",
      packages=find_packages(),
      setup_requires=['cython'],
      install_requires=['cython'],
      test_suite='nose.collector',
      license = 'The MIT License',
      tests_require='nose',
      package_data={'': ['*.pyx', '*.pxd']},
      include_dirs=["."],
)
