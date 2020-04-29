#!/usr/bin/python


from __future__ import print_function
import base64, json, sys, urllib, zlib
from Adafruit_Thermal import *

from urllib2 import urlopen
import lxml as lh
import os
import random




printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

def read_file():
    print("Now reading the file..")
    try:
        f = open("story1.txt", "r")
        for line in f.readlines():
            print(line)
        f.close()



printer.feed(3)
