#!/usr/bin/env python
import os
import parapin
from parapin.CONST import *

import time
usleep = lambda x: time.sleep(x/1000.0)

port = parapin.Port(LPT1, outmode=LP_PIN01|LP_DATA_PINS|LP_PIN16|LP_PIN17)

pierwszy = port.get_pin(1, 2, 3, 4)
drugi = port.get_pin(5, 7, 8, 9)
mazak = port.get_pin(16, 17)

print "Clearing..."
pierwszy.clear()
drugi.clear()
mazak.clear()
raw_input("Connect power and hit return...\n")

kroktime = 1.2 # umie szybciej, ale zalozmy ze to bezpiecznie maksimum

if True:
  i=0
  print "Steppers..."
  while i<600:
    print i
    port.get_pin(1,9).set()
    usleep(kroktime)
    port.get_pin(4,5).clear()
    usleep(kroktime)
    port.get_pin(2,8).set()
    usleep(kroktime)
    port.get_pin(1,9).clear()
    usleep(kroktime)
    port.get_pin(3,7).set()
    usleep(kroktime)
    port.get_pin(2,8).clear()
    usleep(kroktime)
    port.get_pin(4,5).set()
    usleep(kroktime)
    port.get_pin(3,7).clear()
    usleep(kroktime)
    i=i+1
  print "kuniec"

print "Clearing..."
pierwszy.clear()
drugi.clear()
mazak.clear()
