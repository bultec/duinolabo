'''
Name:        mesures_rc
Purpose:      lecture de la tension aux bornes d'un condensateur en fonction du temps
              déclenchement de la charge du condensateur par mise du pin 3 à HIGH
              - en mode lent (arduino envoi des données entre chaque mesure)
              - en mode rapide (arduino envoi des données à la fin des mesures)
             à utiliser avec les programmes condo.ino et condo_rapide.ino
             commandes disponibles: charge, decharge, sauve
Copyright (C) 2023 Philippe Campion
License    GNU GENERAL PUBLIC LICENSE Version 3

Schéma du montage
                                                Pin 4   Pin 5
                                      GND         |       |
 Pin 3                                --+--      +++     +++
  ^                                     |        | |     | |
  |                                     |        | |     | |
  |                              | |    |        +++     +++
  |        +----------+          | |    |         |       |
--+---+----+   R      +---+------+ +----+       --+--   --+--
      |    +----------+   |      | |C           \   /   \   /
      |                   |      | |             \ /     \ /
      |                   |                      -+-     -+-
      |                   |                       |       |
      v                   v                       |       |
       A1                  A0                    -+-     -+-
                                                 GND     GND
'''

from pduino import *

port = 'COM21'

def affiche(T):
    '''
    appelé à chaque mesure
    affiche les données issues du tuple T contenant les valeurs des voies
    '''
    s = 't = {:.2f} s ; E = {:.2f} V ; uc = {:.2f} V'.format(T[0], T[1], T [2])
    print(s)

# --- programme principal ---
arduino = Arduino(port)
try:
    command = ''
    while True:
        last_command = command
        command = input('Entrez une commande : ')
        if command in ['charge', 'decharge']:
            t, E, uc = arduino.mesures_tempo(command, 2, affichage = affiche,
                       fonctions = [lambda x: 5.0*x/1023, lambda x: 5.0*x/1023])
            print()
            affiche_graphe('Evolution des tensions E et uc', 't (s)', 'u (V)',
                            [t, E, uc], taille=(10,8))
        elif command == 'sauve':
            if len(t) > 0 :
                fichier = '{}_condo.csv'.format(last_command)
                ecrit_fichier_csv(fichier, t, E, uc)
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


