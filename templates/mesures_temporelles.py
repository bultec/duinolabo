'''
Commentaires
'''

from pduino import *

port = '...'

def affiche(T):
    '''
    éventuellement appelé à chaque mesure
    affiche les données issues du tuple T contenant les valeurs des voies
    à supprimé si non utilisé
    '''
    s = ...
    print(s)

# --- programme principal ---
arduino = Arduino(port)
try:
    command = ''
    while True:
        last_command = command
        command = input('Entrez une commande : ')
        if command in ['...', '...']:
            ...   = arduino.mesures_tempo(command, ..., affichage = ...)
            print()
            affiche_graphe('...titre...', 't (s)', '...', ...,
                            [t, ..., ...], taille = (10,8))
        elif command == 'sauve':
            if len(t) > 0 :
                fichier = '....csv'
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


