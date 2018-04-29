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

import json

from .datanow import DataNow
from .data import Data
from .datavalues import DataValues
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

        parameters = "&startdate=%s" % startdate
        parameters += "&intervaltype=%s" % intervaltype

        if enddate is not None:
            parameters += "&enddate=%s" % enddate

        if channelid is not None:
            parameters += "&channelid=%d" % channelid

        eliqData = self._tools.get_data_from_eliq(function, parameters)

        jsonData = json.loads(eliqData)
        eliq_data = self._json_to_data(jsonData)
        return eliq_data

    def _json_to_data(self, jsonData):
        """
        Args:
            jsonData: (data)
        Returns:
            list: with DataValues
        """
        eliq_data = Data()
        eliq_data.startdate = jsonData["startdate"]
        eliq_data.intervaltype = jsonData["intervaltype"]
        eliq_data.enddate = jsonData["enddate"]
        eliq_data.channelid = jsonData["channelid"]

        eliq_data.data = []
        for json_data_values in jsonData["data"]:
            data_values = DataValues()
            data_values.avgpower = json_data_values["avgpower"]
            data_values.energy = json_data_values["energy"]
            data_values.temp_out = json_data_values["temp_out"]
            data_values.time_end = json_data_values["time_end"]
            data_values.time_start = json_data_values["time_start"]
            eliq_data.data.append(data_values)

        return eliq_data

    def get_data_now(self, channelid=None):
        """
        Args:
            channelid (int)

        Returns:
            eliqonline.datanow
        """
        function = "datanow"
        parameters = None

        if channelid is not None:
            parameters = "&channelid=%d" % channelid

        eliqData = self._tools.get_data_from_eliq(function, parameters)

        json_data = json.loads(eliqData)
        eliq_data_now = DataNow()
        eliq_data_now.power = float(json_data["power"])
        eliq_data_now.channelid = json_data["channelid"]
        eliq_data_now.createddate = json_data["createddate"]
        return eliq_data_now
