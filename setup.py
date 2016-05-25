#!/usr/bin/env python
from distutils.core import setup

files = [
    "ansible/module_utils",
    "ansible/modules/hashivault",
]

setup(name='ansible-modules-hashivault',
    version='1.1.3',
    description='Ansible Modules for Hashicorp Vault',
    long_description=open("README.rst").read(),
    author='Terry Howe',
    author_email='terrylhowe@example.com',
    url='https://github.com/TerryHowe/ansible-modules-hashivault',
    packages=files,
    install_requires = [
        'hvac',
        'ansible>2.0.0',
    ],
)