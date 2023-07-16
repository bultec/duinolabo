#-------------------------------------------------------------------------------
# Name:        mesures_us
# Purpose:     lecture de données mesurées en fontion du temps
#              en mode rapide (arduino envoi des données à la fin des mesures)
#              à utiliser avec le programme capteur_us_tempo
#              commandes disponibles: mesure, sauve
# Author:      Ph. Campion
# Created:     29/04/2023
#-------------------------------------------------------------------------------
import serial
import time
from py_ardu import *

port = 'COM33'

# --- programme principal ---
def affiche(T):
    s = 't = {:.4f} ms ; E = {}'.format(T[0], int(T[1]))
    print(s)

arduino = serial.Serial(port=port, baudrate=9600, timeout=1)
try:
    command = ''
    while True:
        last_command = command
        command = input('Entrez une commande : ')
        if command in ['mesure']:
            t, E = mesures_tempo(arduino, command, 1, affichage = affiche)
            print()
            affiche_graphe('Evolution de E (entrée digitale)', 't (ms)', 'E',
                            [t, E], taille=(10,7))
        elif command == 'sauve':
            if len(t) > 0 :
                fichier = 'sauve_us.csv'.format(last_command)
                ecrit_fichier_csv(fichier, t, E)
                print('fichier {} créé'.format(fichier))
            else:
                print('pas de mesures effectuées')
        else:
            print('commande non reconnue')
            command = last_command

except KeyboardInterrupt:
    pass

finally:
    arduino.close()


