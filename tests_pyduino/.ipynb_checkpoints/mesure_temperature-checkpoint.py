'''
Name:        mesure_temperature
Purpose:     lecture de températures mesurées en fontion du temps
             par le programme capteur_temperature.ino
Copyright (C) 2023 Philippe Campion
License    GNU GENERAL PUBLIC LICENSE Version 3
'''

from pyduino import *

port = 'COM33'

def affiche(T):
    '''
    appelé à chaque mesure
    affiche les données issuées du tuple T contenant les valeurs des voies
    '''
    s =  't = {:.2f} s ; teta = {:.2f} °C'.format(T[0], T[1])
    print(s)

arduino = Arduino(port)

try:
# important car il n'y a pas delai (input) dans le programme
time.sleep(1)

# --- programme principal ---
try:
    t, teta = mesures_tempo(arduino, 'mesure', 1, affichage = affiche)
    affiche_graphe('Evolution de la température', 't (s)', 'Teta (°C)',[t, teta])
except Exception as e:
    print(e)
    set_command(arduino, 'stop')
    print('erreur')
finally:
    arduino.close()

# ecriture fichier csv
if len(t) > 0 :
    try:
        reponse  = input('Ecrire le fichier temperatures.csv (o/n) : ')
        if reponse == 'o':
            ecrit_fichier_csv('temperatures.csv', t, teta)
            print('fichier créé')
    except KeyboardInterrupt:
        pass


