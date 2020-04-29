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

listofFiles = [' ']

for i in range (1, 50):
listofFiles.append('story' + i + '.txt')

selectedFile = random.choice(listOfFiles)
f = open(selectedFile, 'r')
file_contents = f.read()
printer.print(file_contents)
f.close()

printer.feed(3)
