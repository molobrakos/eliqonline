# Eliq Online API Library

## Information
A simple API library for Eliq Online.
For more information, see Eliq Online API;
https://eliq.zendesk.com/hc/en-us/articles/115002708449-API-Eliq-Online

## Installation
Install with pip
```
$ sudo pip install eliqonline
```

## Code examples
### Current power usage
Getting the current power usage
```python
#! /usr/bin/env python
import eliqonline

access_token = ""
eliq_online = eliqonline.API(access_token)

data_now = eliq_online.get_data_now()
print("Power: %d W" % data_now['power'])
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
data = eliq_online.get_data(start_date, elie_online.INTERVAL_6MIN, stop_date)
if data:
    for item_data in data.data:
        print("%s -> %s: Avg. power: %d W" % (
            item_data['time_start'],
            item_data['time_end'],
            item_data['avgpower']
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

### Using the module directly

```
$ python -m eliqonline now
Current power: 408 w

$ python -m eliqonline week
2018-09-13T00:00:00 - 2018-09-14T00:00:00: average power: 2231 W
2018-09-14T00:00:00 - 2018-09-15T00:00:00: average power: 1346 W
2018-09-15T00:00:00 - 2018-09-16T00:00:00: average power: 1316 W
2018-09-16T00:00:00 - 2018-09-17T00:00:00: average power: 9262 W
2018-09-17T00:00:00 - 2018-09-18T00:00:00: average power: 1371 W
2018-09-18T00:00:00 - 2018-09-19T00:00:00: average power: 1391 W
2018-09-19T00:00:00 - 2018-09-20T00:00:00: average power: 1429 W
```
