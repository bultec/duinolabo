
## Duinolab - juduino  - mesures arduino sous Jupyter

`juduino` permet de créer très simplement des systèmes d'interfaces de mesures graphiques sous jupyter en utilisant le module `pyduino`.

Comme `pyduino`, `judiuno` poermet deux modes de fonctionnement:
            
- Mode 1 : acquisition temporelle : il est possible de mesurer une ou plusieurs voies en fonction du temps et d'appliquer éventuellement une fonction de transfert.
    - en mode lent (arduino envoi des données entre chaque mesure)
    - en mode rapide (arduino envoi des données à la fin des mesures)

Démo avec le notebook `test_circuit_rc.ipynb` et les programmes `condo.ino` ainsi que `condo_rapide.ino`

- Mode 2 : point par point
    - la méthode `set_command()` permet d'envoyer n'importe quelle commande à _Arduino_ et de recevoir la réponse. Elle permet donc d'utiliser toutes les possibilités de commande et de mesure d'_Arduino_.

Le notebook `test_mesures_ponctuelles.ipynb` qui permet la vérification de la loi de _Mariotte_ est un bon exemple d'utilisation.
              
Les mesures peuvent être stockées dans un fichier csv pour exploitation utérieure.

# Fonctions publiques disponibles

## class Interface:
La classe implémente sous jupyter une interface d'acquisition pour arduino utilisant le module pyduino

### Constructeur __init__(self, p_port='', p_grandeurs=[], p_mode='points', p_temps_reel=True)
        initialise la classe
        entrée : p_port -> str : port série auquel est connecté arduino (voir la documentation de pyduino)
                 p_grandeurs -> list : tableau de tuple contenant les grandeurs à mesurer et leurs unités
                                       par exemple:  [('t', 's'), ('E', 'V'), ('uc', 'V')]
                                                     [('V', 'mL'), ('P', 'Pa')]
                 p_mode -> str : 'temporel' ou 'points'
        
### Méthode add_bouton(self, p_texte, p_command)
        ajoute un bouton à la classe
        entrée : p_texte -> str : le texte qui s'affiche sur le bouton
                 p_command -> function : la fonction à exécuter lorsqu'on clique sur le bouton  
        sortie -> ipywidgets.widgets.widget_button.Button : widget contenant le bouton

### Méthode add_saisie(self, p_description, p_valeur="")
        ajoute un une zone de saisie à la classe
        entrée : p_description -> str : le texte de description de la zone de saisie
                 p_valeur -> str : la valeur par défaut dans la zone de saisie 
        sortie -> ipywidgets.widgets.widget_string.Text : widget contenant la zone de saisie

### Méthode affiche(self)
        affiche le widget interface complet
                
### Méthode mesures_tempo(self, chaine, n, affichage=None, fs=[])
        appelle la fonction mesures_tempo du module pyduino
        et récupère les mesures envoyées par Arduino sur la liaison série
        entrée : chaine -> str : la commande à envoyer à Arduino
                fonctions -> list de fonctions (vide par défaut)
                             fonction à appliquer eventuellement sur la grandeur
                             fournie par Arduino
                             par exemple [lambda x: 5.0*x/1023, lambda x: 5.0*x/1023]
            sortie -> tuple : les listes (tableaux) de données
                              le temps sera toujours la première donnée
            exemple: mon_interface = Arduino('COM21', [('t', 's'), ('E', 'V'), ('uc', 'V')], 'temporel')
                     t, E, uc = mon_interface.mesures_tempo('charge', [lambda x: 5.0*x/1023, lambda x: 5.0*x/1023])
    
### Méthode set_command(self, command=''):
        appelle la fonction set_command du module pyduino
        et récupère les mesures envoyées par Arduino sur la liaison série
        
    
### Méthode ajoute_point(self, x, y):
        ajoute un point de coordonnées x, y dans le cas de mesures ponctuelles
        
### Méthode supprime_dernier_point(self):
        supprime le dernier point ajouté dans le cas de mesures ponctuelles
        
### Méthode get_valeurs(self):
        renvoir un tuple qui contient les tableaux de valeurs
        utile dans le cas de mesures ponctuelles pour récupérer les tableaux une fois la série terminée
        sortie -> tuple : les listes (tableaux) de données