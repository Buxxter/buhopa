#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging.config
import netrc
import os, platform
import time

# os_ver_dict = {'mac': 'Darwin', 'linux': 'Linux', 'windows': 'Windows'}
os_platform = platform.system()

if 'Darwin' == os_platform:
    logging.config.fileConfig(fname='log_mac.conf')
    secrets = netrc.netrc()
elif 'Linux' == os_platform:
    logging.config.fileConfig(fname='log_lin')
    secrets = netrc.netrc()
elif 'Windows' == os_platform:
    logging.config.fileConfig(fname='log_win.conf')
    secrets = netrc.netrc(file=os.path.join(os.environ['USERPROFILE'], "_netrc"))
else:
    raise RuntimeError('Unknown Platform {}'.format(os_platform))

logger = logging.getLogger(__name__)
bot = None

def main():
    global bot, logger
    import telegram
    logger = logging.getLogger(__name__)
    master, none_acc, TOKEN = secrets.authenticators('my_temporary_debug_bot')

    logger.debug('master={}'.format(master))

    bot = telegram.TelegramBot(TOKEN)
    bot.master = int(master)


if '__main__' == __name__:

    import argparse

    parser = argparse.ArgumentParser(add_help=True,
                                     usage='buhopa.py {-v|--verbose [debug|info|warning|none]}'
                                     )
    parser.add_argument('-v', '--verbose', type=str, choices=['debug', 'info', 'warning', 'none'], default=None)
    args = parser.parse_args()

    if args.verbose is None:
        pass
    elif 'none' in args.verbose:
        logging.getLogger().setLevel(logging.NOTSET)
    elif 'warning' in args.verbose:
        logging.getLogger().setLevel(logging.WARNING)
    elif 'info' in args.verbose:
        logging.getLogger().setLevel(logging.INFO)
    elif 'debug' in args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    main()

    logger.debug(args)

    bot.message_loop()

    while 1:
        time.sleep(20)
