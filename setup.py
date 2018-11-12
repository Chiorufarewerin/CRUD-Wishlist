'''Setup file'''

import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import find_packages, setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


packages = find_packages()

setup(
    name="CRUD-Wishlist",
    version="0.2",
    author="Chiorufarewerin",
    python_requires='>=3.5',
    author_email="artur1998g@gmail.com",
    description="Simple CRUD application on Python with PyQT5.",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    license="MIT",
    platform="Windows",
    url="https://github.com/Chiorufarewerin/CRUD-Wishlist",
    packages=packages,
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
)
