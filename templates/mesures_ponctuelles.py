'''
Commentaire
'''

import matplotlib.pyplot as plt
import time

from pduino import *

# modifiez le port COM en fonction de votre configuration
port = '...'

def get_mesure():
    '''
    la fonction boucle
     - demande la valeur de l'abscisse x à l'utilisateur,
     - envoie la commande 'mesure' à arduino et reçoit la valeur de l'ordonnée y
     - affiche le couple (x, y)
    On pourrait modifier les noms de variables x et y, mais ce n'est pas forcément nécessaire
    '''
    X, Y = [], []
    saisie = True
    while saisie:
        try:
            # saisie de la aveleur de x
            x =input('Entrer la valeur de ... \n-1 pour supprimer dernier point ')
            if x != '-1':
                x = int(x) # ou x = float(x)
                # mesure de la valeur de y
                y = float(arduino.set_command('mesure'))
                print('... = {:.1f} ... ; ... = {:.2f} ...\n'.format(x, y))
                X.append(x)
                Y.append(y)
            else:
                if len(X) > 0:
                    X.pop()
                    Y.pop()
                    print('Dernier point supprimé\n')
                else:
                    print('Pas de dernier point\n')
        except KeyboardInterrupt:
            saisie = False
        except ValueError:
            print('Erreur de saisie\n')
    return X, Y

# --- programme principal ---
'''création de l'objet arduino et boucle de mesures
   à la sortie de la boucle, le graphe Y = f(X) est affiché
   à la fermeture du graphe, une sauvegarde des données sous forme
   de fichier csv est proposée
'''
arduino = Arduino(port)
# indispensable
time.sleep(1)

'''
Eventuellement, changer les noms X et Y ci-dessous
'''
try:
    X, Y = get_mesure()
    if len(X) >0 :
        affiche_graphe('Courbe Y = f(X)', '$X~(...)$', '$Y~(...)$', [ X, Y])
finally:
    arduino.close()

# ecriture fichier csv
if len(X) > 0 :
    try:
        nom_fic = input('Nom du fichier de sauvegarde (sans l\'entension)\n')
        ecrit_fichier_csv('{}.csv'.format(nom_fic), X, Y)
        print('fichier {}.csv créé'.format(nom_fic))
    except KeyboardInterrupt:
        pass
