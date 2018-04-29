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


class DataNow(object):
    """ Class for Eliq's Data Now function """

    def __init__(self):
        self._channelid = None
        self._createddate = None
        self._power = None
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
            channelid (int):
        """
        if channelid is not None:
            self._channelid = int(channelid)

    @property
    def createddate(self):
        """
        Returns:
            createddate (datetime or None):
        """
        if isinstance(self._createddate, datetime):
            return self._createddate
        else:
            return None

    @createddate.setter
    def createddate(self, createddate):
        """
        Args:
            createddate (str): Date and time (ISO 8601, European)
        """
        self._createddate = self._tools.to_date(createddate)

    @property
    def power(self):
        """
        Returns:
            power (float or None):
        """
        if isinstance(self._power, float):
            return self._power
        else:
            return None

    @power.setter
    def power(self, power):
        """
        Args:
            power (float):
        """
        self._power = float(power)
