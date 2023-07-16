'''
Name:        ultrason_mesure
Purpose:     lecture du temps de parcours d'une onde ultrasonore
             par le programme capteur_us.ino
             utilisation de la bibliothèque pyduino
Author:      Ph. Campion
Created:     08/04/2023
'''

from pyduino import *

# modifiez le port COM en fonction de votre configuration
port ='COM21'

def get_mesure():
    '''
    la fonction boucle
     - demande la distance d capteur-écran à l'utilisateur,
     - envoie la commande 'mesure' à arduino et reçoit le temps de parcours t des ultrasons
     - affiche le couple (d, t)
    '''
    distances, temps = [], []
    saisie = True
    while saisie:
        try:
            d = input('Entrer la distance d en cm (-1 pour supprimer le dernier point)')
            if d != '-1':
                d = int(d)
                # envoie la commande 'mesure' à arduino et reçoit le temps de parcours des ultrasons
                t = int(set_command(arduino, 'mesure')) # en µs
                print('d = {:.1f} cm ; t = {} µs\n'.format(d, t))
                distances.append(d)
                temps.append(t)
            else:
                # supression du dernier point
                if len(distances) > 0:
                    distances.pop()
                    temps.pop()
                    print('Dernier point supprimé\n')
                else:
                    print('Pas de dernier point\n')
        except KeyboardInterrupt:
            # pour sortir du mode mesure
            saisie = False
        except ValueError:
            print('Erreur de saisie\n')
    return distances, temps

# --- programme principal ---
'''création de l'objet arduino et boucle de mesures
   à la sortie de la boucle, le graphe t = f(d) est affiché
   à la fermeture du graphe, une sauvegarde des données sous forme de fichier csv est proposée
'''
arduino =serial.Serial(port=port, baudrate=9600, timeout=1)
try:
    distances, temps = get_mesure()
    if len(distances)>0 :
        affiche_graphe('Courbe d = f(t)', 'd (cm)', 't (µs)', [distances, temps])
finally:
    arduino.close()

# sauvegarde du fichier de mesures au format csv
if len(distances) >0 :
    try:
        nom_fic = input('Nom du fichier de sauvegarde (sans l\'entension)\n')
        ecrit_fichier_csv('{}.csv'.format(nom_fic), distances, temps)
        print('fichier {}.csv créé'.format(nom_fic))
    except:
        pass
