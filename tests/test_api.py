#!/usr/bin/env python
#
#  A library for Eliq Online API
#  Copyright (C) 2015 Magnus F <magnus@fet.nu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

import unittest
import sys
from .unittools import UnitTools
# from datetime import datetime

sys.path.append('.')

import eliqonline


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.unit_tools = UnitTools()
        self.access_token = self.unit_tools.get_random_string()
        self.api = eliqonline.API(self.access_token)

    def test_init(self):
        self.assertEqual(self.access_token, self.api._tools.ACCESS_TOKEN)
