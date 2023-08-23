## Duinolab - pyduino - utilitaire de mesures arduino.

`pyduino` est un module qui simplifie considérablement la réalisation de _mesures temporelles_ ou _point par point_ à l'aide d'une carte _Arduino_.D

Deux modes de fonctionnement sont disponibles:
            
- Mode 1 : acquisition temporelle : il est possible de mesurer une ou plusieurs voies en fonction du temps et d'appliquer éventuellement une fonction de transfert.
    - en mode lent (arduino envoi des données entre chaque mesure)
    - en mode rapide (arduino envoi des données à la fin des mesures)

Démo avec les programmes `mesures_condensateur.py`, `condo.ino` et `condo_rapide.ino`

- Mode 2 : point par point
    - la méthode `set_command()` permet d'envoyer n'importe quelle commande à _Arduino_ et de recevoir la réponse. Elle permet donc d'utiliser toutes les possibilités de commande et de mesure d'_Arduino_.

        Le programme `mariotte_mesure.py`  est un bon exemple d'utilisation.
              
Les mesures peuvent être stockées dans un fichier csv pour exploitation utérieure


## Fonctions disponibles

### liste_ports()
    liste les ports COM connectés

### ecrit_fichier_csv(fichier, *args)
    écrit les données dans un fichier csv
    entrées : fichier -> str nom du fichier (avec extension .csv)
                 args -> list :  les listes (tableaux) de données à enregistrer
    exemple : ecrit_fichier_csv('condensateur.csv', t, E, uc)
    
### lit_fichier(fichier):
    Lit le fichier de mesures et le stocke dans des tableaux
    entrée : fichier -> str : nom du fichier (avec extension .csv)
    sortie -> tuple :  les listes (tableaux) de données
    exemple: t, E, u = lit_fichier('condensateur.csv')

### affiche_graphe(titre, label_x, label_y, donnees, taille=None)
    affiche le graphe
    entrée : titre -> str : le titre du graphe
             label_x et label_y : les labels des axes
             donnees : une liste de listes (tableaux) de données
             le premier tableau contient la donnée en abscisse
             taille -> tuple : taille du graphique (None par defaut) - par exemple taille = (9, 7)
    sortie : affichage du graphe
    exemple: affiche_graphe('Evolution des tensions E et uc', 't (s)', 'u (V)', [t, E, uc])
    
### class Arduino:
#### __init__(port='auto'):
    crée un objet Arduino
    entrée: str: le port COM auquel est connecté auquel est connecté la carte
                 expérimental et non documenté:
                 si port = auto(valeur par defaut),
                 tente de le détecter en utilisant la fonction liste_ports (ne fonctionne pas toujours)
              
#### mesures_tempo(chaine, n, affichage=None, fonctions=[]):
    récupère les mesures envoyées par Arduino sur la liaison série
    entrée : chaine -> str : la commande à envoyer à Arduino
             n -> int : le nombre de voies mesurées (sans compter le temps)
             affichage -> fonction (None par défaut)
                      prend en paramètre le temps et un tuple contenant
                      les voies.
                      est appelée pendant les mesures pour afficher
                      les données
             fonctions -> list de fonctions (vide par défaut)
                      fonction à appliquer eventuellement sur la grandeur
                      fournie par Arduino
                      par exemple [lambda x: 5.0*x/1023, lambda x: 5.0*x/1023]
    sortie -> tuple : les listes (tableaux) de données
                      le temps sera toujours la première donnée
    exemple: arduino = Arduino('COM21')
             t, E, uc = arduino.mesures_tempo('charge', 2, None, [lambda x: 5.0*x/1023, lambda x: 5.0*x/1023])


#### set_command(command=''):
    effectue une mesure ponctuelle sur Arduino ou envoie une commande
        entrée : command -> str : la commande à envoyer à Arduino
                              'mesure' par défaut si non renseigné
        sortie -> str : la valeur renvoyée par Arduino
                        (à surtyper en int ou float selon les cas)
        exemple: arduino = Arduino('COM21')
                 b = int(arduino.set_command('mesure'))

#### close():
    libère le port série
    à utiliser dans un bloc try ... finally pour éviter les problèmes de connection au port série
    exemple:
       arduino = Arduino(port)
       try:
          ...
       finally:
          arduino.close()           
          
