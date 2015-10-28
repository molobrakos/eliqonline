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
from datetime import datetime

sys.path.append('.')

import eliqonline


class TestDataNow(unittest.TestCase):

    def setUp(self):
        self.unit_tools = UnitTools()
        self.data_now = eliqonline.DataNow()

    def test_channelid(self):
        channelid_value = 1234
        self.data_now.channelid = channelid_value
        self.assertEqual(channelid_value, self.data_now.channelid)

    def test_createddate(self):
        createdate_value = datetime.today().replace(microsecond=0)
        createdate_string = createdate_value.strftime('%Y-%m-%dT%H:%M:%S')
        self.data_now.createddate = createdate_string
        self.assertEqual(
            createdate_value,
            self.data_now.createddate
        )

    def test_power(self):
        power = self.unit_tools.get_random_float()
        self.data_now.power = power
        self.assertEqual(power, self.data_now.power)
