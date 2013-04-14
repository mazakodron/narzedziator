#!/usr/bin/env python
import os, code, sys
import parapin
from parapin.CONST import *
port = parapin.Port(LPT1, outmode=LP_PIN01|LP_DATA_PINS|LP_PIN14|LP_PIN16|LP_PIN17)

print "port = parapin.Port(...)"

def DebugKeyboard(banner="Debugger started (CTRL-D to quit)"):

    # use exception trick to pick up the current frame
    try:
        raise None
    except:
        frame = sys.exc_info()[2].tb_frame.f_back

    # evaluate commands in current namespace
    namespace = frame.f_globals.copy()
    namespace.update(frame.f_locals)

    code.interact(banner=banner, local=namespace)

DebugKeyboard()
