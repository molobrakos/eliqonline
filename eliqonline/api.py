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

import json

from .datanow import DataNow
from .data import Data
from .dataitem import DataItem
from .tools import Tools


class API():
    """ API class for Eliq Online API  """

    tools = None

    def __init__(self, access_token):
        self.tools = Tools(access_token)

    def get_data(self, startdate, intervaltype, enddate=None, channelid=None):
        function = "data"

        parameters = "&startdate=%s" % startdate
        parameters += "&intervaltype=%s" % intervaltype

        if enddate is not None:
            parameters += "enddate=%s" % enddate

        if channelid is not None:
            parameters += "&channelid=%d" % channelid

        eliqData = self.tools.get_data_from_eliq(function, parameters)

        if eliqData is None:
            return None
        else:
            jsonData = json.loads(eliqData)
            eliq_data = Data()
            eliq_data.startdate = self.tools.to_date(jsonData["startdate"])
            eliq_data.intervaltype = jsonData["intervaltype"]
            eliq_data.enddate = self.tools.to_date(jsonData["enddate"])
            eliq_data.channelid = jsonData["channelid"]

            eliq_data.data = []

            for json_data_item in jsonData["data"]:
                data_item = DataItem()
                data_item.avgpower = float(json_data_item["avgpower"])
                data_item.energy = float(json_data_item["energy"])
                data_item.temp_out = float(json_data_item["temp_out"])
                data_item.time_end = self.tools.to_date(
                    json_data_item["time_end"]
                )
                data_item.time_start = self.tools.to_date(
                    json_data_item["time_start"]
                )
                eliq_data.data.append(data_item)

            return eliq_data

    def get_data_now(self, channelid=None):
        function = "datanow"
        parameters = None

        if channelid is not None:
            parameters = "&channelid=%d" % channelid

        eliqData = self.tools.get_data_from_eliq(function, parameters)

        if eliqData is None:
            return None
        else:
            json_data = json.loads(eliqData)
            eliq_data_now = DataNow()
            eliq_data_now.power = float(json_data["power"])
            eliq_data_now.channelid = json_data["channelid"]
            eliq_data_now.createddate = self.tools.to_date(
                json_data["createddate"]
            )
            return eliq_data_now
