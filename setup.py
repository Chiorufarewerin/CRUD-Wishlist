'''Setup file'''

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CRUD-Wishlist",
    version="0.2",
    author="Chiorufarewerin",
    author_email="artur1998g@gmail.com",
    description="Simple CRUD application on Python with PyQT5.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chiorufarewerin/CRUD-Wishlist",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
)
