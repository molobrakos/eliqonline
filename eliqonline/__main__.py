#!/usr/bin/env python
"""
ELIQ Online

Usage:
  eliq (-h | --help)
  eliq --version
  eliq [-v|-vv] [options] now
  eliq [-v|-vv] [options] today
  eliq [-v|-vv] [options] daily
  eliq [-v|-vv] [options] monthly
  eliq [-v|-vv] [options] yearly

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
    if args['now']:
        power = api.get_data_now()['power']
        print('Current power: %d kw' % power)
    elif args['today']:
        from datetime import datetime
        now = datetime.now()
        startdate = datetime(year=now.year, month=now.month, day=now.day)
        enddate = datetime(year=now.year, month=now.month, day=now.day,
                           hour=23, minute=59, second=59)
        data = api.get_data(startdate=startdate, enddate=enddate,
                            intervaltype=api.INTERVAL_6MIN)
        for item_data in data['data']:
            print("%s - %s: average power: %4d W" % (
                item_data['time_start'],
                item_data['time_end'],
                item_data['avgpower']
            ))
    elif args['dayly']:
        data = api.get_data()
    elif args['monthly']:
        data = api.get_data()
    elif args['yearly']:
        data = api.get_data()
