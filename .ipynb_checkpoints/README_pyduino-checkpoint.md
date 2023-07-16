# pyduino

`pyduino` est un module à destination des enseignants de physique chimie et de biologie qui permet la réalisation sous _python_ de systèmes de mesures utilisant la carte _Arduino_.

`pyduino` est très efficace et **simplifie considérablement** la réalisation de _mesures temporelles_ ou _point par point_ à l'aide d'une carte _Arduino_.

`pyduino` fait partie d'un ensemble appelé `duinolab` constitué de deux bibliothèques :
- `pyduino` sous python
- `juduino` qui permet de créer très simplement des interfaces de mesures graphiques sous jupyter.

Sans remplacer un oscilloscope ou une interface de mesures, il peut néanmoins effectuer des mesures temporelles jusqu'à une fréquence de 2 ou 3kHz, ce qui est largement suffisant dans 95% des cas des programmes de lycée.

Dans la mesure où toutes les activités sont basées sur le même modèle, (en particulier avec `juduino` sous Jupyter), les élèves, conformément au B.O. Français, se familiarisent rapidement avec l'environnement _python_ pour analyser leurs résultats.

Sont également fournis plusieurs exemples documentés, fonctionnels et testés avec des élèves, applicables au programme Français de sciences physiques dans les classes de lycée.

## Installation

**En cours de _travail_**.

Pour le moment copier `pyduino.py`et éventuellement `juduino.py` dans le même dossier que le projet.

## API références

Le document [reference](./docs/reference.md) détaille les fonctions disponibles dans le module.

## Licence

ici la licence

## Exemples documentés 

### Commande de leds 

Un exemple simple pour commencer : le document [commande_leds](./docs/commande_leds/commande_leds.md) permet de prendre en main la bibliothèque `pyduino` en allumant des leds.

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
