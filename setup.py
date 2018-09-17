#!/usr/bin/env python3
from setuptools import find_packages, setup


def get_version():
    with open('VERSION') as f:
        return f.read()


setup(
    name="organizer",
    version=get_version(),
    url="https://github.com/camenpihor/organizer",
    author="Camen Piho",
    author_email="camenpihor@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirements.in").readlines(),
    tests_require=open("requirements.testing.in").readlines(),
    description="Repository hosting the organizer web app",
    long_description=open("README.md").read(),
)
