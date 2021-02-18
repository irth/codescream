import os

from playsound import playsound

SCREAM_PATH = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "scream1.wav")


def enable():
    from . import hook

def scream():
    playsound(SCREAM_PATH)

import threading
def deprecated(f):
    def wrapped(*args, **kwargs):
        threading.Thread(target=scream).start()
        return f(*args, **kwargs)
    return wrapped
