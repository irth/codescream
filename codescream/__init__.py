import sys
import threading
from playsound import playsound

import os

SCREAM_PATH = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "scream1.wav")


def scream():
    playsound(SCREAM_PATH)


def except_hook(exctype, value, traceback):
    threading.Thread(target=scream).start()
    sys.__excepthook__(exctype, value, traceback)


sys.excepthook = except_hook
