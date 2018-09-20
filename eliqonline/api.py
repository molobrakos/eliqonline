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

import datetime


class API(object):
    """ API class for Eliq Online API  """

    def __init__(self, access_token):
        self._tools = Tools(access_token)

    def get_data(self, startdate, intervaltype, enddate=None, channelid=None):
        """
        Args:
            startdate (str or datetime):
            intervaltype (str or datetime):
                day
                6min
            enddate (str): optional
            channelid (int): optinal

        Returns:
            eliqonline.data
        """
        function = "data"

        if isinstance(startdate, datetime.date):
            startdate = self._tools.date_to_str(startdate)

        if isinstance(enddate, datetime.date):
            enddate = self._tools.date_to_str(enddate)

        parameters = dict(startdate=startdate,
                          intervaltype=intervaltype)

        if enddate is not None:
            parameters.update(enddate=enddate)

        if channelid is not None:
            parameters.update(channelid=channelid)

        return self._tools.get_data_from_eliq(function, parameters)

    def get_data_now(self, channelid=None):
        """
        Args:
            channelid (int)

        Returns:
            eliqonline.datanow
        """
        function = "datanow"
        parameters = {}

        if channelid is not None:
            parameters.update(channelid=channelid)

        return self._tools.get_data_from_eliq(function, parameters)
