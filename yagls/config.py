# -*- coding: utf-8 -*-
import ConfigParser

__config = ConfigParser.ConfigParser()
__config.read("yagls.ini")

try:
    DEBUG = __config.getboolean("Main", "DEBUG")
except ConfigParser.NoOptionError:
    DEBUG = False

try:
    PORT = __config.getboolean("Main", "PORT")
except ConfigParser.NoOptionError:
    PORT = 9999

URL = __config.get("Main", "URL")
if URL[-1] == "/":
    URL = URL[:-1]

FILEPATH = __config.get("Main", "FILEPATH")
