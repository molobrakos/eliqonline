#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import io
import os
import re


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def get_download_url(version):
    return "https://github.com/6d66/eliq/tarball/%s" % version

version = find_version("eliqonline", "__init__.py")
package_name = "eliqonline"

setup(
    name=package_name,
    packages=[package_name],
    version=find_version(package_name, "__init__.py"),
    description='Eliq Online API Library',
    author='6d66',
    author_email='',
    url='https://github.com/6d66/eliq/',
    download_url=get_download_url(version),
    keywords=['Eliq', 'Eliq Online', 'Eliq Online API'],
    classifiers=[],
)
