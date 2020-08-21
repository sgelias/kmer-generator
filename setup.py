import sys
import os
from setuptools import setup, find_packages

try:
    from setuptools import setup
    from setuptools import Command
    from setuptools import Extension
except ImportError:
    sys.exit(
        "We need the Python library setuptools to be installed. "
        "Try runnning: python -m ensurepip"
    )


REQUIRES = [
    "argparse",
    "itertools",
]


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()


setup_args = dict(

    # About package
    name = 'KmerGenerator',
    version = '0.0.1',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['k-mers', 'DNA-Sequences', "Biological-Sequences"],
    url = 'https://github.com/sgelias/kmer-generator.git',
    packages = find_packages(),
    package_dir={'KmerGenerator': 'kmerGenerator'},
    include_package_data = True,

    # About author
    author = 'Samuel Galva\~o Elias',
    author_email = 'sgelias@outlook.com',

    # Language and Licence
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


if __name__ == '__main__':
    setup(install_requires=REQUIRES, **setup_args)
