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


class Tools(object):
    """ Tool class for Eliq Online API  """

    # Base url to Eliq Online API
    BASE_URL = "https://my.eliq.io/api/"

    # Access token for API
    ACCESS_TOKEN = None

    # Date format, (ISO 8601, European)
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

    # Date format for url
    DATE_FORMAT_URL = "%Y-%m-%d %H:%M:%S"

    session = Session()

    def __init__(self, access_token=None):
        if access_token is not None:
            self.ACCESS_TOKEN = access_token

    def get_data_from_eliq(self, function, parameters=None):
        if parameters is None:
            parameters = {}

        api_url = urljoin(
            self.BASE_URL,
            function,
        )

        parameters.update(accesstoken=self.ACCESS_TOKEN)

        return self.session.get(api_url, params=parameters).json()

    def date_to_str(self, date):
        return date.strftime(self.DATE_FORMAT_URL)
