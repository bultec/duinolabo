'''
Name:        ultrasons_mesure_tempo
Purpose:     lecture de données mesurées en fontion du temps
             en mode rapide (arduino envoi des données à la fin des mesures)
             à utiliser avec le programme capteur_us_tempo
             commandes disponibles: mesure, sauve
Copyright (C) 2023 Philippe Campion
License    GNU GENERAL PUBLIC LICENSE Version 3
'''
from pduino import *

port = 'COM30'

def affiche(T):
    '''
    appelé à chaque mesure
    affiche les données issues du tuple T contenant les valeurs des voies
    '''
    s = 't = {:.2e} s ; E = {}'.format(T[0], int(T[1]))
    print(s)

# --- programme principal ---*
'''création de l'objet arduino et boucle de mesures
   à la sortie de la boucle, le graphe E = f(t) est affiché
   à la fermeture du graphe, la commande 'sauve' permet la sauvegarde
   des données sous forme de fichier 'sauve_us.csv'
'''
arduino = Arduino(port)
try:
    command = ''
    t , E = [], []
    while True:
        last_command = command
        command = input('Entrez une commande : ')
        if command in ['mesure']:
            t, E = arduino.mesures_tempo(command, 1, affichage = affiche)
            print()
            affiche_graphe('Evolution de E (entrée digitale)', 't (s)', 'E',
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
    print(len(t))
    arduino.close()


