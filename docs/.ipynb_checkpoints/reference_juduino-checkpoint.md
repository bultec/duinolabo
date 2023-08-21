## juduino - utilitaire de mesures arduino.

Deux modes de fonctionnement:
            
- Mode 1 : acquisition temporelle : il est possible de mesurer une ou plusieurs voies en fonction du temps et d'appliquer éventuellement une fonction de transfert.
    - en mode lent (arduino envoi des données entre chaque mesure)
    - en mode rapide (arduino envoi des données à la fin des mesures)

Démo avec les programmes `mesures_condensateur.py`, `condo.ino` et `condo_rapide.ino`

- Mode 2 : point par point
    - la méthode `set_command()` permet d'envoyer n'importe quelle commande à _Arduino_ et de recevoir la réponse. Elle permet donc d'utiliser toutes les possibilités de commande et de mesure d'_Arduino_.

        Le programme `mariotte_mesure.py`  est un bon exemple d'utilisation.
              
Les mesures peuvent être stockées dans un fichier csv pour exploitation utérieure


## Fonctions disponibles