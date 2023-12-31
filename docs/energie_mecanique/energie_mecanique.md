# Conservation ou non conservation de l'énergie mécanique (en cours de rédaction)

...

#### Important

Comme dans tous les exemples utilisant `pduino` le dialogue entre le programme _python_ et la carte _arduino_  doit impérativement suivre le protocole suivant:

- le programme _python_ envoie une commande sous forme de chaine de caractères sur la liaison série.
- le programme _arduino_ reçoit la commande, la traite et envoie une réponse sur la liaison série.

#### Montage 

Capteur de position Pierron _Grove_ sur A2.

<img src='data/image_1.png' style='width:466px;'>

## Code arduino

Le programme [pendule.ino](../../arduino/pendule/pendule.ino)

- attend l'arrivée d'une commande (`mesure`) sur la liaison série et réagit en conséquence:
- chaque mesure de la température est réalisée à partir de la tension sur A0 et est envoyée sur la liaison série juste après sa réalisation. La série se termine par l'envoi du mot `end`.

## Code python
Le [programme _python_](../../tests/mesure_temperature.py):
- envoie la commande `mesure` sur la liaison série.
- recupère les données lues sur la liaison série.
- affiche le graphe $\theta = f(t)$ 
- à la fermeture du graphe, une sauvegarde des données sous forme de fichier csv est proposée.

**Remarque :** Avant utilisation il peut-être nécessaire de modifier la valeur du port _COM_.

## Exemple d'éxécution
- Avec _python_

...


- Avec _Jupyter_ en utilisant `juduino`

<img src='data/image_2.png'>



## Exemple d'utilisation

Le notebook [temperature_traitement.ipynb](temperature_traitement.ipynb) propose un exemple d'utilisation d'un fichier de mesures dans le but de déterminer la constante de temps de la courbe $\theta = f(t)$ dans le cas de l'évolution de la température d'un corps en contact avec un thermostat.