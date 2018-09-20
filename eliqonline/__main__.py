#!/usr/bin/env python
"""
ELIQ Online

Usage:
  eliq (-h | --help)
  eliq --version
  eliq [-v|-vv] [options] now
  eliq [-v|-vv] [options] today
  eliq [-v|-vv] [options] week
  eliq [-v|-vv] [options] month
  eliq [-v|-vv] [options] year

Options:
  -t <token>      Access token
  -h --help             Show this message
  -v,-vv                Increase verbosity
  --version             Show version
"""

import docopt
import logging
from sys import stderr
from os.path import join, expanduser
from os import environ as env
from yaml import safe_load as load_yaml
from datetime import datetime, timedelta

from eliqonline import API, __version__

LOGFMT = "%(asctime)s %(levelname)5s (%(threadName)s) [%(name)s] %(message)s"
DATEFMT = "%y-%m-%d %H:%M.%S"
LOG_LEVEL = logging.DEBUG
_LOGGER = logging.getLogger(__name__)


# $HOME/.eliqonline and $HOME/.config/eliqonline.conf
CONFIG_FILES = (
    (expanduser('~'), '.eliqonline'),
    (env.get('XDG_CONFIG_HOME',
             join(expanduser('~'), '.config')), 'eliqonline.conf'))


def read_config():
    for directory, filename in CONFIG_FILES:
        try:
            config = join(directory, filename)
            with open(config) as config:
                _LOGGER.debug('Found config file %s', config.name)
                return load_yaml(config)
        except (IOError, OSError):
            continue
    return {}


if __name__ == "__main__":
    args = docopt.docopt(__doc__,
                         version=__version__)

    log_level = [logging.ERROR, logging.INFO, logging.DEBUG][args['-v']]
    logging.basicConfig(level=log_level,
                        stream=stderr,
                        datefmt=DATEFMT,
                        format=LOGFMT)

    config = read_config()
    access_token = args.get('-t') or config.get('accesstoken')
    api = API(access_token=access_token)

    now = datetime.now()

    if args['now']:
        power = api.get_data_now()['power']
        print('Current power: %d w' % power)
        exit()

    if args['today']:
        intervaltype = api.INTERVAL_6MIN
        startdate = datetime(year=now.year, month=now.month, day=now.day)
        enddate = datetime(year=now.year, month=now.month, day=now.day,
                           hour=23, minute=59, second=59)
    else:
        intervaltype = api.INTERVAL_DAY
        enddate = now
        if args['week']:
            startdate = datetime(year=now.year,
                                 month=now.month,
                                 day=now.day) - timedelta(days=7)
        elif args['month']:
            startdate = datetime(year=now.year, month=now.month, day=1)
        elif args['year']:
            startdate = datetime(year=now.year, month=1, day=1)

    data = api.get_data(startdate=startdate, enddate=enddate,
                        intervaltype=intervaltype)

    for item_data in data['data']:
        print("%s - %s: average power: %4s W" % (
            item_data['time_start'],
            item_data['time_end'],
            str(int(item_data['avgpower'])) if item_data['avgpower'] else '?'
        ))
