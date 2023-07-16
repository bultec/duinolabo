# PhyChiPy_ardu

`DuinoLab` est un module à destination des enseignants de physique chimie et de biologie qui permet la réalisation sous _python_ ou _Jupyter_ de systèmes de mesure utilisant la carte _Arduino_.

L'ensemble est constitué de deux bibliothèques :
- `pyduino` qui permet de récupérer de façon simple les mesures effectuées par une carte _Arduino_. 
- `juduino` qui permet de créer sous _Jupyter_ (éventuellement _voilà_) et en quelques lignes de codes une interface graphique utilisant _pyduino_.

Le module peut donc être utilisé dans un environnement python classique ou dans un environnement Jupyter

Sont également fournis plusieurs exemples documentés et fonctionnels applicables au programme Français de sciences physiques dans les classes de lycée.

## Mode d'emploi
**En cours de _travail_**.

## Installation

**En cours de _travail_**. Pour l'instant copier `pyduino.py`et `judiono.py` dans le même dossier que le projet.

## Exemples documentés 

### Commande de leds 

Un exemple simple pour commencer.

- Avec python: le document [allumer des leds](exemples_python/commande_leds/commande_leds.md) utilisant _py_ardu_
- Avec Jupyter : le document [...]() utilisant _jup_ardu_ et _py_ardu_

### Célérité des ultrasons dans l'air - version 1

Un exemple de `mesures point par point` qui utilise directement les données mesurées par le capteur à ultrasons.

- avec python, le document [celerite_ultrasons](exemples_python/celerite_ultrasons/celerite_ultrasons.md) utilisant _py_ardu_
- avec Jupyter : le document [...]()  utilisant _jup_ardu_ et _py_ardu_
- un exemple de TP complet testé avec des élèves qui, de plus, aborde le principe du radar de recul
    - avec python uniquement
    - en utilisant Jupyter

### Mesures de pressions

Un exemple de `mesures point par point` qui utilise un capteur de pression et implémente sa fonction de transfert.

- avec python, le document [loi_mariotte](exemples_python/mesures_pression/loi_mariotte.md) utilisant _py_ardu_
- avec Jupyter : le document [...]()  utilisant _jup_ardu_ et _py_ardu_
- un exemple de TP complet testé avec des élèves
    - avec python uniquement
    - en utilisant Jupyter

### Charge d'un condensateur 
Un exemple de `mesure temporelles lentes`
- le document utilisant _py_ardu_
- le document Jupyter utilisant _jup_ardu_ et _py_ardu_

Un exemple de `mesure temporelles rapides`
- le document utilisant _py_ardu_
- le document Jupyter utilisant _jup_ardu_ et _py_ardu_

### Evolution de la température d'un corps en contact avec un thermostat
Un exemple de `mesure temporelles lentes` qui utilise un capteur de température et implémente sa fonction de transfert
- le document utilisant _py_ardu_
- le document Jupyter utilisant _jup_ardu_ et _py_ardu_

### Célérité des ultrasons dans l'air - version 2
Un exemple de `mesure temporelles très rapides`
- le document utilisant _py_ardu_
- le document Jupyter utilisant _jup_ardu_ et _py_ardu_

### Conservation et non conservation de l'énergie mécanique

Un exemple de réalisation d'un capteur analogique sur un pendule pesant associée à une `mesure temporelle lente`.

- le document utilisant _py_ardu_
- le document Jupyter utilisant _jup_ardu_ et _py_ardu_
- un exemple de TP complet testé avec des élèves
    - avec python uniquement
    - en utilisant Jupyter
    
**Complément:**  A partir des mesures effectuées, un exemple pédagogique de modélisation graphique qui permet à l'élève de comprendre les notions d'amplitude, de période et de phase.

### Mesure de la période d'un pendule (capteur infrarouge - détermination de g)

patati patata

### Couleurs (TP sur internet à voir avec une led RGB)

patati patata

### Biologie (photosynthèse à voir)

patati patata
