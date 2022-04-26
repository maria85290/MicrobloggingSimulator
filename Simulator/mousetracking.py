from pynput.mouse import Listener
from pynput import mouse

from datetime import datetime
import logging
import sys


def on_move(x, y):
    file_object = open('sample.txt', 'a')
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))



def tracking(id_user):
    # Getting the current date and time
    dt = datetime.now()
    ts = datetime.timestamp(dt)

    logging.basicConfig(filename=  "static/filestore/mousetracking/" + str(id_user) + ".log", level=logging.DEBUG, format='%(asctime)s: %(message)s', force=True)
    listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)
    listener.start()

