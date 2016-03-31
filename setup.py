#!/usr/bin/env python
import shutil
import os.path
from distutils.command.build_ext import build_ext
from setuptools import setup, Extension, find_packages
from subprocess import check_call


def build_patchelf():
    try:
        curdir = os.path.abspath(os.curdir)
        os.chdir('patchelf')
        check_call(['./bootstrap.sh'])
        check_call(['./configure'])
        check_call(['make'])
        path = os.path.abspath('src/patchelf')
    finally:
        os.chdir(curdir)
    return path


class build_ext(build_ext):
    def run(self):
        fn = build_patchelf()
        shutil.copy(fn, os.path.join(self.output_dir(), 'patchelf'))

    def output_dir(self):
        if not self.inplace:
            return os.path.join(self.get_finalized_command('build').build_platlib, 'pypatchelf')

        build_py = self.get_finalized_command('build_py')
        package_dir = os.path.abspath(build_py.get_package_dir('pypatchelf'))
        return package_dir


setup(name='pypatchelf',
      version='0.9',
      maintainer="Robert T. McGibbon",
      maintainer_email="rmcgibbo@gmail.com",
      author="Eelco Dolstra",
      author_email="<none>@gmail.com",
      url="https://github.com/nixos/patchelf",
      platforms="Linux",
      description="A small utility to modify the dynamic linker and RPATH of ELF executables",
      classifiers=["Development Status :: 3 - Alpha",
                   "Environment :: Console",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Operating System :: POSIX :: Linux",
                   "Topic :: Software Development"],
      license="GPL",
      entry_points={
          'console_scripts': [
              'patchelf = pypatchelf:main',
              ]},
      packages=find_packages(),
      zip_safe=False,
      ext_modules=[Extension('mock', ['mock'])],
      cmdclass={'build_ext': build_ext})
