#!/usr/bin/python


from __future__ import print_function
import base64, json, sys, urllib, zlib
from Adafruit_Thermal import *

from urllib2 import urlopen
import lxml as lh
import os
import random




printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

x = open('story1.txt')
r=x.read()
    printer.print(x)
    printer.println(' ')
	


printer.feed(3)
