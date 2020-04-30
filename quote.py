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


listOfFiles = ['story1.txt', 'story2.txt', 'story3.txt', 'story4.txt', 'story5.txt', 'story6.txt', 'story7.txt', 'story8.txt',
               'story8.txt', 'story9.txt', 'story10.txt', 'story11.txt', 'story12.txt', 'story13.txt', 'story14.txt', 'story15.txt', 
              'story16.txt', 'story17.txt', 'story18.txt', 'story19.txt', 'story20.txt', 'story21.txt', 'story22.txt', 'story23.txt',
              'story24.txt', 'story25.txt', 'story26.txt', 'story27.txt', 'story28.txt', 'story29.txt', 'story30.txt', 'story31.txt'
              'story32.txt', 'story33.txt', 'story34.txt', 'story35.txt', 'story36.txt', 'story37.txt', 'story38.txt', 'story39.txt'
              'story40.txt', 'story41.txt', 'story42.txt', 'story43.txt', 'story44.txt', 'story45.txt', 'story46.txt', 'story47.txt'
              'story48.txt', 'story49.txt', 'story50.txt', 'story51.txt]

selectedFile = random.choice(listOfFiles)
f = open(selectedFile, 'r')
file_contents = f.read()
printer.print(file_contents)
f.close()

printer.feed(3)
