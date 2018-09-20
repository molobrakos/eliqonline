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

    def _request_data(self, function, parameters=None, channelid=None):
        if not parameters:
            parameters = {}

        api_url = urljoin(
            BASE_URL,
            function,
        )

        parameters.update(accesstoken=self._access_token)

        if channelid:
            parameters.update(channelid=channelid)

        return self._session.get(api_url, params=parameters).json()

    def get_data(self, startdate, intervaltype, enddate=None, channelid=None):
        """
        Args:
            startdate (datetime):
            intervaltype (str):
                day
                6min
            enddate (datetime): optional
            channelid (int): optinal

        Returns:
            eliqonline.data
        """

        if isinstance(startdate, datetime.date):
            startdate = startdate.strftime(DATE_FORMAT)

        if isinstance(enddate, datetime.date):
            enddate = enddate.strftime(DATE_FORMAT)

        parameters = dict(startdate=startdate,
                          intervaltype=intervaltype)

        if enddate:
            parameters.update(enddate=enddate)

        return self._request_data('data', parameters, channelid=channelid)

    def get_data_now(self, channelid=None):
        """
        Args:
            channelid (int)

        Returns:
            eliqonline.datanow
        """
        return self._request_data('datanow', channelid=channelid)
