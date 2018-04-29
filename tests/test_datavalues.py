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

sys.path.append('.')

import eliqonline


class TestDataValues(unittest.TestCase):

    def setUp(self):
        self.unit_tools = UnitTools()
        self.data_values = eliqonline.DataValues()

    def test_avgpower(self):
        avgpower_value = self.unit_tools.get_random_float()
        self.data_values.avgpower = avgpower_value
        self.assertEqual(avgpower_value, self.data_values.avgpower)

    def test_avgpower_none(self):
        self.data_values.avgpower = None
        self.assertEqual(None, self.data_values.avgpower)

    def test_energy(self):
        energy_value = self.unit_tools.get_random_float()
        self.data_values.energy = energy_value
        self.assertEqual(energy_value, self.data_values.energy)

    def test_energy_none(self):
        self.data_values.energy = None
        self.assertEqual(None, self.data_values.energy)

    def test_temp_out(self):
        temp_out_value = self.unit_tools.get_random_float()
        self.data_values.temp_out = temp_out_value
        self.assertEqual(temp_out_value, self.data_values.temp_out)

    def test_temp_out_none(self):
        self.data_values.temp_out = None
        self.assertEqual(None, self.data_values.temp_out)

    def test_time_start(self):
        time_start_value = self.unit_tools.get_datetime_today()
        time_start_string = self.unit_tools.datetime_to_string(time_start_value)
        self.data_values.time_start = time_start_string
        self.assertEqual(time_start_value, self.data_values.time_start)

    def test_time_start_none(self):
        self.data_values.time_start = None
        self.assertEqual(None, self.data_values.time_start)

    def test_time_end(self):
        time_end_value = self.unit_tools.get_datetime_today()
        time_end_string = self.unit_tools.datetime_to_string(time_end_value)
        self.data_values.time_end = time_end_string
        self.assertEqual(time_end_value, self.data_values.time_end)

    def test_time_end_none(self):
        self.data_values.time_end = None
        self.assertEqual(None, self.data_values.time_end)
