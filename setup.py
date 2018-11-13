#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Flask-RESTful',
    version='0.2.5',
    url='https://www.github.com/twilio/flask-restful/',
    author='Kyle Conroy',
    author_email='help@twilio.com',
    description='Simple framework for creating REST APIs',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    test_suite = 'nose.collector',
    #setup_requires=[
    #    'nose==1.3.1',
    #    'mock==1.0.1',
    #    'six==1.5.2',
    #    'blinker==1.3',
    #],
    install_requires=[
        'Flask==0.12.3',
    ],
    # Install these with "pip install -e '.[paging]'" or '.[docs]'
    extras_require={
        'paging': 'pycrypto>=2.6',
        'docs': 'sphinx',
    }
)
