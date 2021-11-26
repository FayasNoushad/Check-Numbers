import os
import setuptools


def requirements(file="requirements.txt"):
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


setuptools.setup(
    name="Check-Numbers",
    version="1.0.5",
    description="Numbers checker",
    long_description=readme(),
    long_description_content_type="text/markdown",
    download_url="https://github.com/FayasNoushad/Check-Numbers/releases/latest",
    license="MIT",
    author="Fayas Noushad",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Tracker": "https://github.com/FayasNoushad/Check-Numbers/issues",
        "Source": "https://github.com/FayasNoushad/Check-Numbers"
    },
    python_requires=">=3.6",
    py_modules=['check_numbers'],
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=requirements()
)
