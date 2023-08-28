#-------------------------------------------------------------------------------
# Name:        mesures_pendule (sans modélisation)
# Purpose:     lecture de données mesurées en fontion du temps
#              en mode lent (arduino envoi des données entre chaque mesure)
#              à utiliser avec le programme pendule.ino
#              commandes disponibles: mesures, sauve
# Author:      Ph. Campion
# Created:     08/03/2023
#-------------------------------------------------------------------------------
import numpy as np
from math import pi
import serial
import time
from py_ardu import *

port = 'COM4'

def ecrit_fichier_csv(t, voie, fichier):
    t = np.array(t)
    voie = np.array(voie)
    maxi, mini = max(voie), min(voie)
    milieu = mini + (maxi - mini) // 2
    # conversion en radians
    teta = 2*pi * (voie - milieu) / 1024
    R = 41.5e-2
    x = R * np.sin(teta)
    y = R * (1 - np.cos(teta))
    with open(fichier,'w') as f :
        for i in range(len(t)):
            f.write("{};{};{}\n".format(t[i], x[i], y[i]))
    f.close()

# --- programme principal ---
t = []
arduino = serial.Serial(port=port, baudrate=9600, timeout=1)
try:
    while arduino.readline().decode() != '' : {}
    command = ''
    while True:
        last_command = command
        command = input('Entrez une commande : ')
        if command in  ['mesures']:
            t, voie_2 = mesures_tempo(arduino, command, 1)
            affiche_graphe('Mesures effectuées', 't (s)', '???', [t, voie_2])
        elif command == 'sauve':
            if len(t) > 0 :
                fichier = '{}_pendule.csv'.format(last_command)
                ecrit_fichier_csv(t, voie_2, fichier)
                print('fichier {} créé'.format(fichier))
            else:
                print('pas de mesures effectuées')
        else:
            print('commande non reconnue')
            command = last_command

except Exception as e:
    print(e)

except KeyboardInterrupt:
    pass

finally:
    arduino.close()


