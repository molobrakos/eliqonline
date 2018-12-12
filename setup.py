#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import re


def find_version(path):
    with open(path) as f:
        version_match = re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M
        )
        if version_match:
            return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def get_download_url(version):
    return "https://github.com/6d66/eliq/tarball/%s" % version


version = find_version("./eliqonline.py")
package_name = "eliqonline"

setup(
    name=package_name,
    version=version,
    description="Eliq Online API Library",
    author="6d66",
    author_email="",
    url="https://github.com/6d66/eliq/",
    download_url=get_download_url(version),
    install_requires=list(open("requirements.txt").read().strip().split()),
    keywords=["Eliq", "Eliq Online", "Eliq Online API"],
    classifiers=[],
    scripts=["eliqonline"],
    py_modules=["eliqonline"],
    extras_require={"console": ["docopt"]},
)
