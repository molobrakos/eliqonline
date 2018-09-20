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

import datetime
from requests import Session
from requests.compat import urljoin
import datetime


# Base url to Eliq Online API
BASE_URL = "https://my.eliq.io/api/"

# Date format for url
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class API(object):
    """ API class for Eliq Online API  """

    INTERVAL_6MIN = "6min"
    INTERVAL_DAY = "day"

    def __init__(self, access_token):
        self._session = Session()
        self._access_token = access_token

    def _request_data(self, function, parameters=None):
        if parameters is None:
            parameters = {}

        api_url = urljoin(
            BASE_URL,
            function,
        )

        parameters.update(accesstoken=self._access_token)

        return self._session.get(api_url, params=parameters).json()

    def get_data(self, startdate, intervaltype, enddate=None, channelid=None):
        """
        Args:
            startdate (datetime):
            intervaltype (str):
                day
                6min
            enddate (str): optional
            channelid (int): optinal

        Returns:
            eliqonline.data
        """
        startdate = startdate.strftime(DATE_FORMAT)
        if enddate:
            enddate = enddate.strftime(DATE_FORMAT)

        parameters = dict(startdate=startdate,
                          intervaltype=intervaltype)

        if enddate is not None:
            parameters.update(enddate=enddate)

        if channelid is not None:
            parameters.update(channelid=channelid)

        return self._request_data('data', parameters)

    def get_data_now(self, channelid=None):
        """
        Args:
            channelid (int)

        Returns:
            eliqonline.datanow
        """
        parameters = {}

        if channelid is not None:
            parameters.update(channelid=channelid)

        return self._request_data('datanow', parameters)
