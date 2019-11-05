from setuptools import setup
from setuptools import find_packages
from os import path

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open(path.join('README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
   name='zopyx.check_ssl_domains',
   version='1.0.5',
   long_description=long_description,
   description='Check expiration date of SSL/TLS certs on web host',
   author='Andreas Jung',
   author_email='info@zopyx.com',
   install_requires=required,
   packages=find_packages(),
   entry_points = {
        'console_scripts': ['ssl-check-domains=zopyx.checker:main']
   }
)

