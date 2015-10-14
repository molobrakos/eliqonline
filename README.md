(Not complete!) Eliq Online API Libary

```python
#! /usr/bin/env python

import eliqonline

access_token = ""
eliq_online = eliqonline.API(access_token)

data_now = eliq_online.get_data_now()
if data_now:
    print data_now.power
    print data_now.channelid
    print data_now.createddate
```
