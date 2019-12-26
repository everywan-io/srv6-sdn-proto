# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from setuptools.command.install import install
# To use a consistent encoding
from codecs import open
from os import path
# To generate python grpc stubs
import os
import sys
import subprocess
import glob

PYTHON_PATH = sys.executable

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

        
open('./srv6_sdn_proto/__init__.py', 'a').close()
# Generate python grpc stubs from proto files

print('Generation of python gRPC stubs')
args = "-I. --proto_path=./srv6_sdn_proto --python_out=. --grpc_python_out=. srv6_sdn_proto/*.proto"
result = subprocess.call("%s -m grpc_tools.protoc %s" % (PYTHON_PATH, args), shell=True)
if result != 0:
    exit(-1)

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
setup(
    name='srv6-sdn-proto',  
    version='1.0-beta',
    description='SRv6 SDN Proto',  # Required
    long_description=long_description,
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='',  # Optional
    packages=['srv6_sdn_proto'],  # Required
    install_requires=[
        'setuptools',
        'grpcio>=1.19.0',
        'grpcio-tools>=1.19.0',
        'protobuf>=3.7.1',
        'six>=1.12.0'
    ]
)