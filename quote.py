#!/usr/bin/python


from __future__ import print_function
import base64, json, sys, urllib, zlib
from Adafruit_Thermal import *

from urllib2 import urlopen
import lxml as lh
import os
import random




printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

f = open('story49', 'r')
file_contents = f.read()
printer.print (file_contents)
f.close()


printer.feed(3)
