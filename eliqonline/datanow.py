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


class DataNow():
    """ Class for Eliq's Data Now function """

    def __init__(self):
        self.channelid = None
        self.createddate = None
        self.power = None

    @property
    def channelid(self):
        return self.channelid

    @channelid.setter
    def channelid(self, value):
        self.channelid = value

    @property
    def createddate(self):
        return self.createddate

    @createddate.setter
    def createddate(self, value):
        self.createddate = value

    @property
    def power(self):
        return self.power

    @power.setter
    def power(self, value):
        self.power = value
