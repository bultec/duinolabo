#-------------------------------------------------------------------------------
# Name:        mesures_rc_dec
# Purpose:     lecture de la tension aux bornes d'un condensateur en fonction du temps
#              avec déclenchement manuel de la charge du condensateur par bouton poussoir
#               - en mode lent (arduino envoi des données entre chaque mesure)
#               - en mode rapide (arduino envoi des données à la fin des mesures)
#              à utiliser avec les programmes condo_dec.ino et condo_rapide_dec.ino
#              commandes disponibles: charge, sauve
# Author:      Ph. Campion
# Created:     02/04/2023
#-------------------------------------------------------------------------------

''' Schéma du montage
                                          GND
                   Pin 7                 --+--               Pin 4   Pin 5
                     |    +----------+     |       GND         |       |
                     +----+ 100 k    +-----+       --+--      +++     +++
                     |    +----------+               |        | |     | |
       bouton        |                               |        | |     | |
          ++         |                        | |    |        +++     +++
         -++-        |  +----------+          | |    |         |       |
+5V  ----    ------+-+--+   R      +---+----+-+ +----+       --+--   --+--
                   |    +----------+   |    | | |C           \   /   \   /
                   |                   |    | | |             \ /     \ /
                   |                   |    |                 -+-     -+-
                   |                   |    |       ++         |       |
                   v                   v    |      -++-        |       |
                   A1                  A0   +------    --------+-     -+-
                                                  bouton      GND     GND
'''

from pyduino import *

port = 'COM21'

# --- programme principal ---
def affiche(T):
    s = 't = {:.2f} s ; E = {:.2f} V ; uc = {:.2f} V'.format(T[0], T[1], T [2])
    print(s)

arduino = Arduino(port)
try:
    command = ''
    while True:
        last_command = command
        command = input('Entrez une commande : ')
        if command in ['charge']:
            t, E, uc = arduino.mesures_tempo(command, 2, affichage = affiche,
                       fonctions = [lambda x: 5.0*x/1023, lambda x: 5.0*x/1023])
            print()
            affiche_graphe('Evolution des tensions E et uc', 't (s)', 'u (V)',
                            [t, E, uc], taille=(12,8))
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


