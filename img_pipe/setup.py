from setuptools import setup
from setuptools.command.install import install
import os, subprocess

# This was part of the img_pipe package and forces conda to install the vtk and pyqt4 packages. However, these packages
# are already distributed with the anaconda package. If you run into problems with the installation of vtk/pyqt you
# could try to uncomment the lines of code below and create a shellscript 'dependencies.sh. with:
# #! /bin/bash
#
# conda install -y vtk==6.3.0
# conda install -y pyqt==4.11.4


# class MyInstall(install):
#
#     def run(self):
#         install.run(self)
#         os.system("./img_pipe/dependencies.sh")
#

setup(
    name='img_pype',
    version='1.0',
    packages=['', 'plotting', 'SupplementalFiles', 'SupplementalScripts', 'surface_warping_scripts',
              'electrode-registration-app', 'electrode-registration-app.Old', 'electrode-registration-app.app',
              'electrode-registration-app.app.ui', 'electrode-registration-app.app.core',
              'electrode-registration-app.tests'],
    url='https://github.com/MichaelLebrand/img_pype',
    license='',
    author='Liberty Hamilton, Falcon Day. Edited by Michael leibbrand',
    author_email='michael_leib@hotmail.com',
    description='Chang Lab/Liberty Hamilton\'s img_pipe as edited by Michael Leibbrand',
    setup_requires=['cython','numpy','scipy']
)
