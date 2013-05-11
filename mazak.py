#!/usr/bin/env python
import os
import parapin
from parapin.CONST import *

import time
usleep = lambda x: time.sleep(x/1000.0)

port = parapin.Port(LPT1, outmode=LP_PIN01|LP_DATA_PINS|LP_PIN14|LP_PIN16|LP_PIN17)

pierwszy = port.get_pin(1, 2, 3, 4)
drugi = port.get_pin(5, 7, 8, 9)
mazak = port.get_pin(16, 17)

port.get_pin(14).clear()

print "Clearing..."
pierwszy.clear()
drugi.clear()
mazak.clear()
raw_input("Connect power and hit return...\n")

kroktime = 1.2 # umie szybciej, ale zalozmy ze to bezpiecznie maksimum

if True:
  i=0
  while i<50:
    print i
    port[16].set()
    usleep(150)
    port[16].clear()
    usleep(200)
    port[17].set()
    usleep(50)
    port[17].clear()
    usleep(200)
    i=i+1
  print "kuniec"

print "Clearing..."
pierwszy.clear()
drugi.clear()
mazak.clear()
port.get_pin(14).set()
