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


class TestData(unittest.TestCase):

    def setUp(self):
        self.unit_tools = UnitTools()
        self.data = eliqonline.Data()

    def test_channelid(self):
        channelid_value = 123
        self.data.channelid = channelid_value
        self.assertEqual(channelid_value, self.data.channelid)

    def test_channelid_none(self):
        self.assertEqual(None, self.data.channelid)

    def test_startdate(self):
        startdate_value = datetime.today().replace(microsecond=0)
        startdate_string = startdate_value.strftime('%Y-%m-%dT%H:%M:%S')
        self.data.startdate = startdate_string
        self.assertEqual(
            startdate_value,
            self.data.startdate
        )

    def test_startdate_none(self):
        self.assertEqual(None, self.data.startdate)
