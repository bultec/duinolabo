'''
Name:       commande_leds
Purpose:    démo de la fonction set_command de la bibliothèque pyduino
            fonctionne avec le programme arduino leds
            commandes dispos: rouge, verte, stop
Copyright (C) 2023 Philippe Campion
License    GNU GENERAL PUBLIC LICENSE Version 3

Schéma du montage
    Pin 4   Pin 5
      |       |
     +++     +++
     | |     | |
     | |     | |
     +++     +++
      |       |
    --+--   --+--
    \   /   \   /
     \ /     \ /
     -+-     -+-
      |       |
      |       |
     -+-     -+-
     GND     GND 
'''

from pyduino import *

# modifiez le port COM en fonction de votre configuration
port = 'COM21'

try:
    '''Il y a 3 façons de créer l'instance de la classe Arduino'''
    # arduino = Arduino('auto')
    # arduino = Arduino(port)
    arduino = Arduino()

    while True:
        command = input('Entrez une commande : ')
        result = arduino.set_command(command)
        print(result)

except KeyboardInterrupt:
    pass

finally:
    arduino.close()