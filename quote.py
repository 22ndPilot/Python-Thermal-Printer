#!/usr/bin/python


from __future__ import print_function
import base64, json, sys, urllib, zlib
from Adafruit_Thermal import *

from urllib2 import urlopen
import lxml as lh
import os
import random




printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

from pathlib import Path
fileContent = Path('./story1.txt').read_text()
printer.print(fileContent)

printer.feed(3)
