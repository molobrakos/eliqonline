#!/usr/bin/env python

""" A library that provides a Python interface to the Eliq Online API"""

__author__ = "6D66"
__version__ = "0.0.1"

from .api import API
from .datanow import DataNow
from .data import Data

__all__ = ["API", "DataNow", "Data"]
