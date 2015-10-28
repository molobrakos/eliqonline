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

import urllib
from datetime import datetime


class Tools():
    """ Tool class for Eliq Online API  """

    # Base url to Eliq Online API
    BASE_URL = "https://my.eliq.se/api"

    # Access token for API
    ACCESS_TOKEN = None

    # Date format, (ISO 8601, European)
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

    def __init__(self, access_token=None):
        if access_token is not None:
            self.ACCESS_TOKEN = access_token

    def get_data_from_eliq(self, function, parameters=None):
        if parameters is None:
            parameters = ""

        # Build API request url
        api_url = "%s/%s?accesstoken=%s%s" % (
            self.BASE_URL,
            function,
            self.ACCESS_TOKEN,
            parameters
        )

        api_open = urllib.urlopen(api_url)
        api_code = api_open.getcode()
        api_content = api_open.read()
        api_content = api_content.decode('utf-8')

        # On http 400 (bad request), print out the error and return None.
        if api_code == 400:
            print(api_content)
            return None
        else:
            return api_content

    def maybe_to_date(self, date_string):
        if date_string is not None:
            return self.to_date(date_string)
        else:
            return None

    def to_date(self, date_string):
        return datetime.strptime(
            date_string,
            self.DATE_FORMAT
        )

    def maybe_to_float(self, float_string):
        if float_string is not None:
            return float(float_string)
        else:
            return None
