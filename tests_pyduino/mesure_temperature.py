'''
Name:        mesure_temperature
Purpose:     lecture de températures mesurées en fontion du temps
             par le programme capteur_temperature.ino
Copyright (C) 2023 Philippe Campion
License    GNU GENERAL PUBLIC LICENSE Version 3
'''

from pyduino import *
import time

port = 'COM34'

def affiche(T):
    '''
    appelé à chaque mesure
    affiche les données issues du tuple T contenant les valeurs des voies
    '''
    s =  't = {:.2f} s ; theta = {:.2f} °C'.format(T[0], T[1])
    print(s)

arduino = Arduino(port)
# important car il n'y a pas delai (input par exemple) dans le programme
time.sleep(1)

# --- programme principal ---
try:
    t, theta = arduino.mesures_tempo('mesure', 1, affichage = affiche)
    affiche_graphe('Evolution de la température', 't (s)', 'Theta (°C)',[t, theta])
finally:
    arduino.close()

# ecriture fichier csv
if len(t) >0 :
    try:
        nom_fic = input('Nom du fichier de sauvegarde (sans l\'entension)\n')
        ecrit_fichier_csv('{}.csv'.format(nom_fic), t, theta)
        print('fichier {}.csv créé'.format(nom_fic))
    except KeyboardInterrupt:
        pass


