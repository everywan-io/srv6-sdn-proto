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

#class PostInstallCommand(install):
#    """Post-installation for installation mode."""
#    def run(self):
#        generate_proto()
#        install.run(self)
        
def generate_proto():
    # Generate python grpc stubs from proto files
    proto_files = glob.glob("srv6_sdn_proto/*.proto")

    print('Generation of python grpc stubs')
    print(proto_files)
    for file in proto_files:
        args = "--proto_path=./srv6_sdn_proto --python_out=./srv6_sdn_proto --grpc_python_out=./srv6_sdn_proto {0}".format(file)
        result = subprocess.call("%s -m grpc_tools.protoc %s" % (PYTHON_PATH, args), shell=True)
        print("grpc generation result for '{0}': code {1}".format(file, result))
        if result != 0:
            exit(-1)

#os.mknod("srv6_sdn_proto/__init__.py")

generate_proto()

install_requires = [
    'grpcio>=1.21.0',
    'grpcio-tools>=1.21.0',
    'protobuf>=3.8.0',
    'setuptools'
]

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
    install_requires=install_requires,
    #cmdclass={
    #    'install': PostInstallCommand,
    #},
)