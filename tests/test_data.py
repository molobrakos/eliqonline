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

    def test_enddate(self):
        enddate_value = datetime.today().replace(microsecond=0)
        enddate_string = enddate_value.strftime('%Y-%m-%dT%H:%M:%S')
        self.data.enddate = enddate_string
        self.assertEqual(
            enddate_value,
            self.data.enddate
        )

    def test_enddate_none(self):
        self.assertEqual(None, self.data.enddate)

    def test_intervaltype_day(self):
        intervaltype = "day"
        self.data.intervaltype = intervaltype
        self.assertEqual(intervaltype, self.data.intervaltype)

    def test_intervaltype_6min(self):
        intervaltype = "6min"
        self.data.intervaltype = intervaltype
        self.assertEqual(intervaltype, self.data.intervaltype)

    def test_intervaltype_none(self):
        intervaltype = "ost"
        self.data.intervaltype = intervaltype
        self.assertEqual(None, self.data.intervaltype)

    def test_data(self):
        n_data_values = 10
        for i in range(1, n_data_values):
            data_values = eliqonline.DataValues()
            self.data.data.append(data_values)

        self.assertEqual(n_data_values, len(self.data.data)+1)

    def test_data_none(self):
        self.data.data = False
        self.assertEqual(None, self.data.data)
