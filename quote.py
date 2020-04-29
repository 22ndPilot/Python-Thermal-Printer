#!/usr/bin/python


from __future__ import print_function
import base64, json, sys, urllib, zlib
from Adafruit_Thermal import *

from urllib2 import urlopen
import lxml as lh
import os
import random

url = "https://github.com/22ndPilot/Python-Thermal-Printer/blob/master/test/story15"
page = urllib.urlopen(url)
doc = str(page.read())
index = doc.find("<p class=\"# start">")
doc = doc[index:-1]
index = doc.find("<p>")
doc = doc[index+3:-1]
end = doc.find("<p class=\"# end">")
result = doc[:end].replace("</p>", "").replace("\\t",
    "").replace("\\n","").replace("\\r", "").replace("<p>",
        "\n").replace("&nbsp;"," ").replace("&ldquo;","\"").replace("&rdquo;",
            "\"").split("<br />")


printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
for x in result:
    printer.print(x)
    printer.println(' ')


printer.feed(3)
