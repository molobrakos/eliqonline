#!/usr/bin/env python
#
# A library for Eliq Online API
# 6d66
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
from mock import patch, Mock

sys.path.append('.')

import eliqonline


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.unit_tools = UnitTools()
        self.access_token = self.unit_tools.get_random_string()
        self.api = eliqonline.API(self.access_token)

    def test_init(self):
        self.assertEqual(self.access_token, self.api._tools.ACCESS_TOKEN)

    @patch("eliqonline.tools.Tools.get_data_from_eliq")
    def test_get_data_now(self, mock_urlopen):
        channelid_value = 123
        createddate_value = self.unit_tools.get_datetime_today()
        power_value = float(
            "{0:.5f}".format(
                self.unit_tools.get_random_float()
            )
        )

        json_test_data = dict(
            channelid = channelid_value,
            createddate = createddate_value,
            power = power_value)

        mock_urlopen.return_value = json_test_data

        data_now = self.api.get_data_now(channelid_value)

        self.assertEqual(channelid_value, data_now.channelid)
        self.assertEqual(createddate_value, data_now.createddate)
        self.assertEqual(power_value, data_now.power)

    @patch("eliqonline.tools.Tools.get_data_from_eliq")
    def test_get_data(self, mock_urlopen):
        channelid_value = 12345
        startdate_value = self.unit_tools.get_datetime_today()

        enddate_value = self.unit_tools.get_datetime_today()
        intervaltype_value = "day"

        json_test_data = dict(
            channelid = channelid_value,
            startdate = startdate_value,
            enddate = enddate_value,
            intervaltype = intervaltype_value,
            data = [
                dict(avgpower=2442.0,
                     energy=58619.0,
                     temp_out=-0.79166666666666663,
                     time_start=startdate_value,
                     time_end=enddate_value)
            ]
        )

        mock_urlopen.return_value = json_test_data

        data = self.api.get_data(
            startdate_value,
            intervaltype_value,
            enddate_value,
            channelid_value
        )

        self.assertEqual(startdate_value, data.startdate)
        self.assertEqual(intervaltype_value, data.intervaltype)
        self.assertEqual(enddate_value, data.enddate)
        self.assertTrue(isinstance(data.data, list))
