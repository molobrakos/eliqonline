# Eliq Online API Libary
[![Build Status](https://travis-ci.org/6D66/eliq.svg)](https://travis-ci.org/6D66/eliq)

## Information
A simple API libary for Eliq Online.
For more information see Eliq Online API forum thread; 
https://my.eliq.se/knowledge/sv-SE/49-eliq-online/299-eliq-online-api

## Installation
Install with pip
```
sudo pip install eliqonline
```

## Code examples
### Current power usage
Getting the current powerusage
```python
#! /usr/bin/env python
import eliqonline

access_token = ""
eliq_online = eliqonline.API(access_token)

data_now = eliq_online.get_data_now()
if data_now:
    print("Power: %d W" % data_now.power)
```
Example output:
```
Power: 496 W
```

### Data for a specific date
Getting power usage data for the date 2015-10-28
```python
#! /usr/bin/env python
import eliqonline

access_token = ""
eliq_online = eliqonline.API(access_token)

start_date = "2015-10-28 00:00"
stop_date = "2015-10-29 00:00"
data = eliq_online.get_data(start_date, "6min", stop_date)
if data:
    for item_data in data.data:
        print("%s -> %s: Avg. power: %d W" % (
            item_data.time_start.time(),
            item_data.time_end.time(),
            item_data.avgpower
        ))

```
Example output:
```
...
09:06:00 -> 09:12:00: Avg. power: 1970 W
09:12:00 -> 09:18:00: Avg. power: 1970 W
09:18:00 -> 09:24:00: Avg. power: 1598 W
09:24:00 -> 09:30:00: Avg. power: 1358 W
...
```
