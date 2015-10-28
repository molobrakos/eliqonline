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


class Data():
    """ Class for Eliq's Data function """

    def __init__(self):
        self.channelid = None
        self.startdate = None
        self.enddate = None
        self.intervaltype = None
        self.data = None

    @property
    def channelid(self):
        return self.channelid

    @channelid.setter
    def channelid(self, value):
        self.channelid = value

    @property
    def startdate(self):
        return self.startdate

    @startdate.setter
    def startdate(self, value):
        self.startdate = value

    @property
    def enddate(self):
        return self.enddate

    @enddate.setter
    def enddate(self, value):
        self.enddate = value

    @property
    def intervaltype(self):
        return self.intervaltype

    @intervaltype.setter
    def intervaltype(self, value):
        self.intervaltype = value

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, value):
        self.data = value
