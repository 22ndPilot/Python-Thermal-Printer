#!/usr/bin/python


from __future__ import print_function
import base64, json, sys, urllib, zlib
from Adafruit_Thermal import *

from urllib2 import urlopen
import lxml as lh
import os
import random

url = "https://raw.githubusercontent.com/22ndPilot/Python-Thermal-Printer/master/test/story15"
page = urllib.urlopen(url)
doc = str(page.read())

result = doc[:end]


printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
for x in result:
    printer.print(x)
    printer.println(' ')


printer.feed(3)
