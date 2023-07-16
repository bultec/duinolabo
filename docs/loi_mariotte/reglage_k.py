#-------------------------------------------------------------------------------
# Name:        reglage_k
# Purpose:     ajustement de k pour le programme mariotte.ino
# Author:      Ph. Campion
# Created:     29/12/2022
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import serial
import time

def get_mesure():
    saisie = True
    while saisie:
        try:
            k = input('Entrer la valeur de k : ')
            k = float(k)
            # mesure de la pression
            arduino.write('mes\n'.encode())
            time.sleep(1)
            data = arduino.readline()
            b = int(data.decode()[:-2])
            uref = 5.0;
            u = b / 1023 * uref;
            p = (u-k)*7000 / (uref-k);
            print('k = {:.4f} ; P = {:.2f} hPa\n'.format(k, p))
        except KeyboardInterrupt:
            saisie = False
        except ValueError:
            print('Erreur de saisie\n')

# --- programme principal ---
arduino =serial.Serial(port='COM6', baudrate=9600, timeout=1)
while arduino.readline().decode() != '' : {}
try:
    get_mesure()
finally:
    arduino.close()
