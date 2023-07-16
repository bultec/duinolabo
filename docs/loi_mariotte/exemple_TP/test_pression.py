#!/usr/bin/env python
# coding: utf-8

from pyduino import *

port = 'COM34'

arduino = Arduino(port)

# indispensable
time.sleep(1)

pression, i = 0, 0
n = 5
try:
    for j in range (0, n):
        b = int(arduino.set_command('mesure'))
        print('.', end='')
        y = b / 1024 * 5
        k = 0.155
        p = (y - k)  * 7000 / (4.7-k)
        if p <= 1500:
            i = i + 1
            pression = pression + p
    print()
    print('P = {:.2f} hPa'.format(pression/i))
finally:
    arduino.close()




