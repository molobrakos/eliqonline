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

from sys import version_info
from aiohttp import ClientTimeout
from datetime import timedelta, date
from urllib.parse import urljoin
import logging

MIN_PYTHON_VERSION = (3, 5, 3)

_ = version_info >= MIN_PYTHON_VERSION or exit(
    "Python %d.%d.%d required" % MIN_PYTHON_VERSION
)

__version__ = "1.2.1"

_LOGGER = logging.getLogger(__name__)

# Base url to Eliq Online API
BASE_URL = "https://my.eliq.io/api/"

# Date format for url
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

TIMEOUT = timedelta(seconds=30)


class API:
    """ API class for Eliq Online API  """

    INTERVAL_6MIN = "6min"
    INTERVAL_DAY = "day"

    def __init__(self, session, access_token):
        _LOGGER.debug("Using %s version %s", __file__, __version__)
        self._session = session
        self._access_token = access_token

    async def _request_data(self, function, parameters=None, channelid=None):
        if not parameters:
            parameters = {}

        api_url = urljoin(BASE_URL, function)

        parameters.update(accesstoken=self._access_token)

        if channelid:
            parameters.update(channelid=channelid)

        async with self._session.get(
            api_url,
            params=parameters,
            timeout=ClientTimeout(total=TIMEOUT.seconds),
        ) as response:
            response.raise_for_status()
            return await response.json()

    async def get_data(
        self, startdate, intervaltype, enddate=None, channelid=None
    ):
        if isinstance(startdate, date):
            startdate = startdate.strftime(DATE_FORMAT)

        if isinstance(enddate, date):
            enddate = enddate.strftime(DATE_FORMAT)

        parameters = dict(startdate=startdate, intervaltype=intervaltype)

        if enddate:
            parameters.update(enddate=enddate)

        return await self._request_data(
            "data", parameters, channelid=channelid
        )

    async def get_data_now(self, channelid=None):
        return await self._request_data("datanow", channelid=channelid)
