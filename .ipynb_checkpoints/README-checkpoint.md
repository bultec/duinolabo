# pyduino

`pyduino` est un module à destination des enseignants de physique chimie et de biologie qui permet la réalisation sous _python_ de systèmes de mesures utilisant la carte _Arduino_.

`pyduino` est très efficace et **simplifie considérablement** la réalisation de _mesures temporelles_ ou _point par point_ à l'aide d'une carte _Arduino_.

`pyduino` fait partie d'un ensemble appelé `duinolab` constitué de deux bibliothèques :
- `pyduino` sous python
- `juduino` qui permet de créer très simplement des systèmes d'interfaces de mesures graphiques sous jupyter.


![](data/image_2.svg)

Sans remplacer un oscilloscope ou une interface de mesures, le système peut néanmoins effectuer des mesures temporelles jusqu'à une fréquence de 2 ou 3kHz, ce qui est largement suffisant dans 95% des cas des programmes de lycée.

Dans la mesure où toutes les activités sont basées sur le même modèle, (en particulier avec `juduino` sous Jupyter), les élèves, conformément au B.O. Français, se familiarisent rapidement avec l'environnement _python_ pour analyser leurs résultats.

Sont également fournis plusieurs exemples documentés, fonctionnels et testés avec des élèves, applicables au programme Français de sciences physiques dans les classes de lycée.

## Installation

**En cours de _développement_**.

Pour le moment copier les fichiers `pyduino.py`et éventuellement `juduino.py` dans le même dossier que le projet.

## API références

Le document [reference](./docs/reference.md) détaille les fonctions disponibles dans le module.

## Licence

GNU General Public License v3.0 

## Exemples documentés 

### Commande de leds 

Un exemple simple pour commencer : le document [commande_leds](./docs/commande_leds/commande_leds.md) permet de prendre en main la bibliothèque `pyduino` en allumant des leds.

### Célérité des ultrasons dans l'air - version 1

Un exemple de `mesures point par point` qui utilise directement les données mesurées par le capteur à ultrasons. Conforme au programme de la spécialité physique-chimie en première.

- avec python, le document [celerite_ultrasons](./docs/celerite_ultrasons/celerite_ultrasons.md) utilisant `pyduino`
- avec Jupyter : si vous avez installé `juduino` le document [./dev/ultrasons_mesures.ipynb](./dev/ultrasons_mesures.ipynb)  utilisant _jupduino_ et _pyduino_
- un exemple de TP complet testé avec des élèves qui, de plus, aborde le principe du radar de recul  [./docs/celerite_ultrasons/exemple_TP/tp_ultrasons.md](./docs/celerite_ultrasons/exemple_TP/tp_ultrasons.md)

### Charge d'un condensateur 
Un exemple de `mesure temporelles lentes ou rapides` conforme au programme de la spécialité physique-chimie en terminale.
- le document utilisant _pyduino_ : [circuit_rc](./docs/circuit_rc/circuit_rc.md)
- avec Jupyter : si vous avez installé `juduino` le document [./dev/test_circuit_rc.ipynb](./dev/test_circuit_rc.ipynb)

### Célérité des ultrasons dans l'air - version 2
Un exemple de `mesure temporelles très rapides` conforme au programme de physique-chimie en seconde.
- le document utilisant `pyduino` : [celerite_ultrasons_tempo](./docs/ultrasons_tempo/celerite_ultrasons_tempo.md)
- avec Jupyter : si vous avez installé `juduino` le document [./dev/test_ultrasons_tempo.ipynb](./dev/test_ultrasons_tempo.ipynb)

### Mesures de pressions

Un exemple de `mesures point par point` qui utilise un capteur de pression et implémente sa fonction de transfert. Conforme au programme de la spécialité physique-chimie en première.

- le document utilisant `pyduino` : [loi_mariotte](./docs/loi_mariotte/loi_mariotte.md) détaille el protocole et contient un exemple de TP complet testé en classe.
- avec Jupyter : si vous avez installé `juduino` : le document [./dev/pressions_mesures.ipynb](./dev/pressions_mesures.ipynb) est un bon exemple de mesures point par point.