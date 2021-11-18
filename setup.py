import os
import pathlib
from setuptools import setup, find_packages


def requirements(file="requirements.txt") -> list:
    if os.path.isfile(file):
        with open(file, encoding="utf-8") as r:
            return [i.strip() for i in r]
    else:
        return []


def readme(file="README.md"):
    if os.path.isfile(file):
        with open(file, encoding="utf8") as r:
            return r.read()
    else:
        return ""


setup(
    name="Check-Numbers",
    version="1.0.3",
    author="FayasNoushad",
    long_description=readme(),
    long_description_content_type="text/markdown",
    description="A numbers check python module",
    license="MIT",
    url="https://github.com/FayasNoushad/Check-Numbers",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=requirements(),
    python_requires=">=3.6"
)
