from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.3'
DESCRIPTION = 'Making pygame apps easier'

# Setting up
setup(
    name="guiElements",
    version=VERSION,
    author="ricardoquinteladev",
    description=DESCRIPTION,
    readme="README.md",
    packages=find_packages(),
    install_requires=['pygame'],
    keywords=['python', 'pygame', 'game', 'app', 'gui'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)