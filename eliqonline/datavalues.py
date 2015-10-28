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


class DataValues():
    """ Class for Eliq's Data values """

    def __init__(self):
        self.avgpower = None
        self.energy = None
        self.temp_out = None
        self.time_start = None
        self.time_end = None

    @property
    def avgpower(self):
        return self.avgpower

    @avgpower.setter
    def avgpower(self, value):
        self.avgpower = value

    @property
    def energy(self):
        return self.energy

    @energy.setter
    def energy(self, value):
        self.energy = value

    @property
    def temp_out(self):
        return self.temp_out

    @temp_out.setter
    def temp_out(self, value):
        self.temp_out = value

    @property
    def time_start(self):
        return self.time_start

    @time_start.setter
    def time_start(self, value):
        self.time_start = value

    @property
    def time_end(self):
        return self.time_end

    @time_end.setter
    def time_end(self, value):
        self.time_end = value
