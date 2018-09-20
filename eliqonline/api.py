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
from requests import Session
from requests.compat import urljoin
import datetime


# Base url to Eliq Online API
BASE_URL = "https://my.eliq.io/api/"

# Date format for url
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

session = Session()

def get_data_from_eliq(accesstoken, function, parameters=None):
    if parameters is None:
        parameters = {}

    api_url = urljoin(
        BASE_URL,
        function,
    )

    parameters.update(accesstoken=accesstoken)

    return session.get(api_url, params=parameters).json()

def date_to_str(date):
    return date.strftime(DATE_FORMAT)


class API(object):
    """ API class for Eliq Online API  """

    def __init__(self, access_token):
        self._access_token = access_token

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
            startdate = date_to_str(startdate)

        if isinstance(enddate, datetime.date):
            enddate = date_to_str(enddate)

        parameters = dict(startdate=startdate,
                          intervaltype=intervaltype)

        if enddate is not None:
            parameters.update(enddate=enddate)

        if channelid is not None:
            parameters.update(channelid=channelid)

        return get_data_from_eliq(self._access_token, function, parameters)

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

        return get_data_from_eliq(self._access_token, function, parameters)
