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

from .tools import Tools
from datetime import datetime


class DataValues(object):
    """ Class for Eliq's Data values """

    def __init__(self):
        """
        DataValues:
            _avgpower: average power in Watt
            _energy: total power in Watt
            _temp_out: temperature outside
            _time_start: date and time of start
            _time_end: date and time of end
            _tools: tools
        """
        self._avgpower = None
        self._energy = None
        self._temp_out = None
        self._time_start = None
        self._time_end = None
        self._tools = Tools()

    @property
    def avgpower(self):
        if isinstance(self._avgpower, float):
            return self._avgpower
        else:
            return None

    @avgpower.setter
    def avgpower(self, avgpower):
        self._avgpower = self._tools.maybe_to_float(avgpower)

    @property
    def energy(self):
        if isinstance(self._energy, float):
            return self._energy
        else:
            return None

    @energy.setter
    def energy(self, energy):
        self._energy = self._tools.maybe_to_float(energy)

    @property
    def temp_out(self):
        if isinstance(self._temp_out, float):
            return self._temp_out
        else:
            return None

    @temp_out.setter
    def temp_out(self, temp_out):
        self._temp_out = self._tools.maybe_to_float(temp_out)

    @property
    def time_start(self):
        if isinstance(self._time_start, datetime):
            return self._time_start
        else:
            return None

    @time_start.setter
    def time_start(self, time_start):
        self._time_start = self._tools.maybe_to_date(time_start)

    @property
    def time_end(self):
        if isinstance(self._time_end, datetime):
            return self._time_end
        else:
            return None

    @time_end.setter
    def time_end(self, time_end):
        self._time_end = self._tools.maybe_to_date(time_end)
