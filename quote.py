#!/usr/bin/python


from __future__ import print_function
import base64, json, sys, urllib, zlib
from Adafruit_Thermal import *

from urllib2 import urlopen
import lxml as lh
import random

import sys
import os
import random

path = sys.argv[1]

def randomize_file():
	return random.choice(os.listdir("test"))

def print_random_filename(random_file):
	random_filename = random_file.split("")[0]
	print random_filename

random_file = random.choice(os.listdir("test"))

if random_file.startswith('.'):
	new_random_file = randomize_file()
	print_random_filename(new_random_file)
else:
	print_random_filename(random_file)

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
for x in result:
    printer.print(x)
    printer.println(' ')


printer.feed(3)
