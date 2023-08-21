## Loi de Mariotte - Mode d'emploi

Un exemple de `mesures point par point` qui utilise un capteur de pression et implémente sa fonction de transfert.

### Montage

Une seringue qui emprisonne une quantité d'air de volume $V$ à la pression atmosphérique est reliée au capteur de pression par l'intermédiaire d'un tube souple. On fait varier le volume d'air $V$ en agissant sur la seringue et on recueille la pression mesurée par le capteur.

<table style="display:inline-block">
<tr><td><img src='data/image_7.png' style = "height: 200px;"></td><td><img src='data/image_8.jpg' style = "height : 200px;"></td></tr>
</table>

### Code arduino

Comme précédemment, le programme doit:
- après l'arrivée de la commande `mesure` sur la liaison série, effectuer une mesure de la pression.
- envoyer cette valeur sur la liaison série

Deux cas de figures sont possible en fonction de l'aspect pédagogique désiré:

1. Le programme arduino applique la fonction de transfert du capteur et envoie sur la liaison série une valeur réelle de la pression.

Voir à cet effet le code source [capteur_pression_complet](../../arduino/capteur_pression_complet/capteur_pression_complet.ino).

Dans ce cas la ligne de commande du programme _python_ se résume à 

```python
P = int(arduino.set_command('mesure'))
```

2. Le programme arduino envoie la valeur de la tension  relevée sur l'entrée analogique.

Voir à cet effet le code source [capteur_pression](../../arduino/capteur_pression/capteur_pression.ino).

Dans ce cas le code du programme _python_ doit calculer la valeur de P:

```python
b = int(arduino.set_command('mesure'))
# calcul de la valeur de P
P = ...
```

**Remarque** Si nécessaire, la fonction `command` de la bibliothèque `pyduino` permet d'appliquer directement une fonction à la valeur lue sur la liaison série.

### Code python

Algorithme du code [programme _python_](../../tests_pyduino/mariotte_mesure.py):

- Tant qu'il y a des points à mesurer, le programme:
    - demande à l'utilisateur la valeur $V$ du volume de gaz emprisonné.
    - envoie la commande `mesure` sur la liaison série.
    - lorsqu'il reçoit la réponse envoyée par la carte, affiche le couple  $(V, P)$.
- à la sortie de la boucle, le graphe $P = f(V)$ est affiché.
- à la fermeture du graphe, une sauvegarde des données sous forme de fichier csv est proposée.


**Remarque :** Avant utilisation il est nécessaire de modifier la valeur du port _COM_ 

### Exemple de résultats

<img src='data/image_10.png'>


**Remarque**

Si vous utilisez _Jupyter_ et `juduino` un exemple de mesures sous _Jupyter_ est donné dans le notebook [tests_juduino/pressions_mesures.ipynb](../../tests_juduino/pressions_mesures.ipynb)

### Exemple d'utilisation

Le protocole [tp_mariotte.md](exemple_TP/tp_mariotte.md) ainsi que le notebook [mariotte_traitement.ipynb](mariotte_traitement.ipynb) et proposent des exemples de TP et de traitement des données.