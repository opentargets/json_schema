
import os

try:
    from setuptools import setup
except ImportError:
    from distutils import setup

long_description = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

setup(
    name="cttv.input.model",
    version="1.2",
    description=long_description.split("\n")[0],
    long_description=long_description,
    author="Gautier Koscielny",
    author_email="gautierk@targetvalidation.org",
    url="https://github.com/CTTV/json_schema",
    #packages=find_packages('.'),
    #package_dir = {'': '.'},
    #namespace_packages = ["cttv", "cttv.input"],    
    packages=[ "cttv.model","cttv.model.core","cttv.model.bioentity","cttv.model.evidence","cttv.model.evidence.core","cttv.model.evidence.phenotype","cttv.model.evidence.linkout","cttv.model.evidence.drug","cttv.model.evidence.genetics","cttv.model.evidence.association_score" ],
    license="Apache2",
    classifiers=[
        "License :: Apache 2",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)

