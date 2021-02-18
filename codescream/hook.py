import sys
import threading
from playsound import playsound
from . import scream

import os


def except_hook(exctype, value, traceback):
    threading.Thread(target=scream).start()
    sys.__excepthook__(exctype, value, traceback)


sys.excepthook = except_hook
