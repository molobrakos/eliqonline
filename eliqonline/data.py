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

from datetime import datetime
from .tools import Tools


class Data(object):
    """ Class for Eliq's Data function """

    def __init__(self):
        """
        Data:
            _channelid: channel id.
            _startdate: start date.
            _enddate: end date.
            _intervaltype: type of inteval, day or 6min.
            _data: list of DataValues
            _tools: tools
        """
        self._channelid = None
        self._startdate = None
        self._enddate = None
        self._intervaltype = None
        self._data = []
        self._tools = Tools()

    @property
    def channelid(self):
        """
        Returns:
            channelid (int or None):
        """
        if isinstance(self._channelid, int):
            return self._channelid
        else:
            return None

    @channelid.setter
    def channelid(self, channelid):
        """
        Args:
            channelid (int)
        """
        self._channelid = int(channelid)

    @property
    def startdate(self):
        """
        Returns:
            startdate (datetime or None):
        """
        if isinstance(self._startdate, datetime):
            return self._startdate
        else:
            return None

    @startdate.setter
    def startdate(self, startdate):
        """
        Args:
            startdate (str): Date and time (ISO 8601, European)
        """
        self._startdate = self._tools.to_date(startdate)

    @property
    def enddate(self):
        """
        Returns:
            enddate (datetime or None):
        """
        if isinstance(self._enddate, datetime):
            return self._enddate
        else:
            return None

    @enddate.setter
    def enddate(self, enddate):
        """
        Args:
            enddate (str): Date and time (ISO 8601, European)
        """
        self._enddate = self._tools.to_date(enddate)

    @property
    def intervaltype(self):
        """
        Returns:
            intervaltype (str or None): "day", "6min", None
        """
        if self._intervaltype == "day" or self._intervaltype == "6min":
            return self._intervaltype
        else:
            return None

    @intervaltype.setter
    def intervaltype(self, intervaltype):
        """
        Args:
            intervaltype (str):
        """
        self._intervaltype = intervaltype

    @property
    def data(self):
        """
        Returns:
            data (list): with eliqonline.datavalues
        """
        if isinstance(self._data, list):
            return self._data
        else:
            return None

    @data.setter
    def data(self, data):
        """
        Args:
            data (list): with eliqonline.datavalues
        """
        self._data = data
