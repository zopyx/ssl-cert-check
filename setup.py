from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
   name='zopyx.check_ssl_domains',
   version='1.0',
   description='Check SSL domains',
   author='Andreas Jung',
   author_email='info@zopyx.com',
   packages=['zopyx'],  #same as name
   install_requires=required
)

