#!/usr/bin/python


from __future__ import print_function
import base64, json, sys, urllib, zlib
from Adafruit_Thermal import *

from urllib2 import urlopen
import lxml as lh
import os
import random




printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
  def getFileContent("22ndPilot/Python-Thermal-Printer/blob/master/story1.txt"):
    with open("22ndPilot/Python-Thermal-Printer/blob/master/story1.txt", 'r') as theFile:
        # Return a list of lines (strings)
        # data = theFile.read().split('\n')
        
        # Return as string without line breaks
        # data = theFile.read().replace('\n', '')
        
        # Return as string
        data = theFile.read()
        return data

printer.print getFileContent('./story1.txt')


printer.feed(3)
