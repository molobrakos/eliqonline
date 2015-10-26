Eliq Online API Libary

```python
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import eliqonline

access_token = ""
eliq_online = eliqonline.API(access_token)

data_now = eliq_online.get_data_now()
if data_now:
    print "Data Now:"
    print "Power: %d W" % data_now.power

print "---"

date = "2015-10-25"
data = eliq_online.get_data(date, "day")
if data:
    print "Data for %s:" % date
    for item_data in data.data:
        print "Avg. power: %d W" % item_data.avgpower
        print "Energy: %0.2f kWh" % float(item_data.energy/1000)
```

Output:
```
Data Now:
Power: 496 W
---
Data for 2015-10-25:
Avg. power: 1070 W
Energy: 26.76 kWh
```
