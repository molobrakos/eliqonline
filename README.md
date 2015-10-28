# Eliq Online API Libary
[![Build Status](https://travis-ci.org/6D66/eliq.svg)](https://travis-ci.org/6D66/eliq)

## Information
Just a simple API libary for Eliq Online.
For more informations see Eliq Online API Thread; 
https://my.eliq.se/knowledge/sv-SE/49-eliq-online/299-eliq-online-api


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
### Example output:
```
Power: 496 W
```
