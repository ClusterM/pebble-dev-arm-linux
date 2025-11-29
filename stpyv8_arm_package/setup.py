#!/usr/bin/env python3

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="stpyv8",
    version="13.1.201.22",
    author="ARM Build Assistant",
    author_email="",
    description="STPyV8 compatibility layer for ARM processors using Duktape engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=['STPyV8'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
    ],
    keywords="javascript v8 stpyv8 dukpy duktape arm",
    python_requires=">=3.9",
    install_requires=[
        "dukpy>=0.5.0",
    ],
    project_urls={
        "Bug Reports": "",
        "Source": "",
    },
)