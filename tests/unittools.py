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

import random
from datetime import datetime


class UnitTools():
    def get_random_string(self):
        return ''.join(random.choice('0123456789ABCDEF') for i in range(16))

    def get_random_float(self):
        return random.uniform(1.5, 1.9)

    def get_datetime_today(self):
        return datetime.today().replace(microsecond=0)

    def datetime_to_string(self, date):
        return date.strftime('%Y-%m-%dT%H:%M:%S')
