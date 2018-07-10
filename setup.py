# -*-coding:utf-8-*-

"""
    a library for create verification-code

    url: https://github.com/kylescript/vc
    Author: kyle.script@gmail.com
"""

from setuptools import setup, find_packages

setup(
    name='vc',
    version='2018.07.10',
    keywords='verification code',
    description='a library for create verification-code',
    license='MIT License',
    url='https://github.com/kylescript/vc',
    author='kyle',
    author_email='kyle.script@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=['Image>=1.5.20']
)
