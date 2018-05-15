#!/usr/bin/env python
"""
ELIQ Online

Usage:
  eliq (-h | --help)
  eliq --version
  eliq [-v|-vv] [options] datanow

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

    if args['datanow']:
        api = API(access_token=access_token)
        power = api.get_data_now().power
        print('Current power: %d kw' % power)
