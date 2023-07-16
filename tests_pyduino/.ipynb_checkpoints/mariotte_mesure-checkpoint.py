'''
Name:        mariotte_mesure
Purpose:     lecture de pressions par le programme mariotte.ino
             utilisation de la bibliothèque pyduino
Copyright (C) 2023 Philippe Campion
License    GNU GENERAL PUBLIC LICENSE Version 3
'''

import matplotlib.pyplot as plt
import time

from pyduino import *

# modifiez le port COM en fonction de votre configuration
port ='COM8'

def get_mesure():
    '''
    la fonction boucle
     - demande le volume v de gaz emprisonné à l'utilisateur,
     - envoie la commande 'mesure' à arduino et reçoit la pression p
     - affiche le couple (v, p)
    '''
    V, P = [], []
    saisie = True
    while saisie:
        try:
            v =input('Entrer la valeur de V (entre 0 et 60 mL)\n\
-1 pour supprimer dernier point ')
            if v != '-1':
                v = int(v)
                # mesure de la pression
                b = int(arduino.set_command('mesure'))
                #print(b)
                uref = 5.0;
                u = b / 1024 * uref;
                # valeur à modifier éventuellement
                k = 0.114
                p = (u-k)*7000 / (uref-k);
                print('V = {:.1f} mL ; P = {:.2f} hPa\n'.format(v, p))
                V.append(v)
                P.append(p)
            else:
                if len(V) > 0:
                    V.pop()
                    P.pop()
                    print('Dernier point supprimé\n')
                else:
                    print('Pas de dernier point\n')
        except KeyboardInterrupt:
            saisie = False
        except ValueError:
            print('Erreur de saisie\n')
    return V, P

# --- programme principal ---
'''création de l'objet arduino et boucle de mesures
   à la sortie de la boucle, le graphe P = f(V) est affiché
   à la fermeture du graphe, une sauvegarde des données sous forme
   de fichier csv est proposée
'''
arduino = Arduino(port)

try:
    V, P = get_mesure()
    if len(V) >0 :
        affiche_graphe('Courbe V= f(P)', '$V~(m^3)$', '$P~(Pa)$', [ V, P])
finally:
    arduino.close()

# ecriture fichier csv
if len(V) >0 :
    try:
        nom_fic = input('Nom du fichier de sauvegarde (sans l\'entension)\n')
        ecrit_fichier_csv('{}.csv'.format(nom_fic), V, P)
        print('fichier {}.csv créé'.format(nom_fic))
    except KeyboardInterrupt:
        pass


