#!/usr/bin/python


from __future__ import print_function
import base64, json, sys, urllib, zlib
from Adafruit_Thermal import *

from urllib2 import urlopen
import lxml as lh
import os
import random
import json
import glob
import uuid




printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

listOfFiles = [story1, story2, story3, story4, story5]
selectedFile = random.choice(listOfFiles)
f = open(selectedFile, 'r')
printer.print (file_contents)
f.close()

printer.feed(3)
