# Duinolabo

`Duinolabo` est un module à destination des enseignants de physique chimie et de biologie qui permet la réalisation sous _python_ de systèmes de mesures utilisant la carte _Arduino_.

Ce module est très efficace et **simplifie considérablement** la réalisation de _mesures temporelles_ ou _point par point_ à l'aide d'une carte _Arduino_.

`Duinolabo ` est constitué de deux bibliothèques :
- `pduino` qui fonctionne sous python
- `juduino` qui permet de créer très simplement des systèmes d'interfaces de mesures graphiques sous jupyter.

![](data/image_2.svg)

Sans remplacer un oscilloscope ou une interface de mesures, le système peut néanmoins effectuer des mesures temporelles de 100 ou 200 points jusqu'à une fréquence de 40kHz, ce qui est largement suffisant dans la plupart des cas du programmes de lycée.

Dans la mesure où toutes les activités sont basées sur le même modèle, (en particulier avec `juduino` sous Jupyter), les élèves, conformément au B.O. Français, se familiarisent rapidement avec l'environnement _python_ pour analyser leurs résultats.

Sont également fournis plusieurs exemples documentés, fonctionnels et testés avec des élèves, applicables au programme Français de sciences physiques dans les classes de lycée.

## Installation

- Si vous travaillez uniquement avec un IDE _phyton_ (edupython, thonny, spyder, ect...), dans la console de votre environnement python, tapez:
```
    pip install pduino
```
- Si vous travaillez avec Jupyter, dans la console de votre environnement Jupyter, tapez
```
    pip install pduino
```
puis 
```
    pip install juduino
```    

## API références

Le document [reference_pduino](./docs/reference_pduino.md) détaille les fonctions disponibles dans le module _pduino_.

Le document [reference_juduino](./docs/reference_juduino.md) détaille les fonctions disponibles dans le module _juduino_.

## Licence

GNU General Public License v3.0 

## Exemples documentés 

### Commande de leds 

Un exemple simple pour commencer : le document [commande_leds](./docs/commande_leds/commande_leds.md) permet de prendre en main les bibliothèques `pduino` et éventuellement `juiduino` en allumant des leds.

##### Vidéos de démonstration 
- [Duinolabo - Prise en main - Commande de leds](https://youtu.be/ylRu36BADV0?si=N6qFN60a0jkB5NF6)
- [Commandes de leds utilisant Jupyter sous Duinolabo](https://youtu.be/8cVDwGVCikA?si=Rral8xjLYSj9t-5n)

### Célérité des ultrasons dans l'air - version 1

Un exemple de `mesures point par point` qui utilise directement les données mesurées par le capteur à ultrasons. Conforme au programme de la spécialité physique-chimie en première.

- avec python, le document [celerite_ultrasons](./docs/celerite_ultrasons/celerite_ultrasons.md) utilisant `pduino`
- en complément, si vous avez installé `juduino` le document [./tests_juduino/ultrasons_mesures.ipynb](./tests_juduino/ultrasons_mesures.ipynb) utilisant _jupduino_ et _pduino_ permet de travailler sous Jupyter.
- un exemple de TP complet testé avec des élèves qui, de plus, aborde le principe du radar de recul  [./docs/celerite_ultrasons/exemple_TP/tp_ultrasons.md](./docs/celerite_ultrasons/exemple_TP/tp_ultrasons.md)

##### Vidéos de démonstration 

- [Célérité des ultrasons - Mesures ponctuelles avec python](https://youtu.be/b0E0GAu-kEI)
- [Célérité des ultrasons - Mesures ponctuelles avec Jupyter](https://youtu.be/Cjb4Xy14cHE)

### Charge d'un condensateur 
Un exemple de `mesure temporelles lentes ou rapides` conforme au programme de la spécialité physique-chimie en terminale.
- le document utilisant _pduino_ : [circuit_rc](./docs/circuit_rc/circuit_RC.md)
- en complément si vous avez installé `juduino` le document [./tests_juduino/test_circuit_rc.ipynb](./tests_juduino/test_circuit_rc.ipynb), est un bon exemple d'utilisation de Jupyter pour des mesures temporelles.

##### Vidéos de démonstration 

- [Mesures Arduino sur un circuit RC en langage python](https://youtu.be/OjGNy7Ilt34?si=ANy3mu_vvgNzEa9O)
- [Mesures Arduino sur un circuit RC sous Jupyter](https://youtu.be/2p_p6vEm0SE?si=005Ij-iCH5Erwyhk)
- [Charge rapide et déclenchée d'un condensateur en python](https://youtu.be/-3oRcjGYXro?si=tWH72LcwHsWh2Kd0)
- [Charge rapide et déclenchée d'un condensateur sous Jupyter](https://youtu.be/ECt2jFk4a60?si=BKC8fsqc-JioHCbU)

### Célérité des ultrasons dans l'air - version 2
Un exemple de `mesure temporelles très rapides` conforme au programme de physique-chimie en seconde.

- le document utilisant `pduino` : [celerite_ultrasons_tempo](./docs/ultrasons_tempo/celerite_ultrasons_tempo.md)

- en complément, si vous avez installé `juduino` le document [./tests_juduino/test_ultrasons_tempo.ipynb](./tests_juduino/test_ultrasons_tempo.ipynb) permet de travailler sous Jupyter.

##### Vidéos de démonstration 

- [Célérité des ultrasons - Mesures temporelles rapides avec python](https://youtu.be/hFFfyKpyjAI?si=sj6GxtPjxv22Pzwk)
- [Célérité des ultrasons - Mesures temporelles rapides avec Jupyter](https://youtu.be/zmUIsWZbqgs?si=ddo_OSdLHClMzjvj)

### Mesures de pressions
Un exemple de `mesures point par point` qui utilise un capteur de pression et implémente sa fonction de transfert. Conforme au programme de la spécialité physique-chimie en première.

- le document utilisant `pduino` : [loi_mariotte](./docs/loi_mariotte/loi_mariotte.md) détaille le protocole de la manipulation et contient un exemple de TP testé en classe.
- en complément, si vous avez installé `juduino`, le document [./tests_juduino/pressions_mesures.ipynb](./tests_juduino/pressions_mesures.ipynb) est un bon exemple de mesures point par point avec Jupyter.

##### Vidéos de démonstration 

- [Loi de Mariotte - Mesures de pression ponctuelles avec python](https://youtu.be/k_7H3wbGkHA?si=6YUrwszzvmSZ9OEC)
- [Loi de Mariotte - Mesures de pression ponctuelles avec Jupyter](https://youtu.be/oGAZk-o1qiE?si=hlrxQBMGzxCnOfiQ)

### Evolution de la température d'un corps en contact avec un thermostat
Un exemple de `mesure temporelles lentes` qui utilise un capteur de température et implémente sa fonction de transfert. Conforme au programme de la spécialité physique-chimie en terminale.
- le document [evolution_temperature](./docs/evolution_temperature/evolution_temperature.md)  utilisant `pduino` détaille le protocole de la manipulation.
- en complément, si vous avez installé `juduino`, le document [./tests_juduino/test_temperature_tempo.ipynb](./tests_juduino/test_temperature_tempo.ipynb) est un bon exemple d'utilisation de Jupyter pour des mesures temporelles.

##### Vidéos de démonstration 

- [Mesures temporelles de températures sous python](https://youtu.be/jKU0WSlJMjs)
- [Mesures temporelles de températures sous Jupyter](https://youtu.be/XpT9Kb6uw1Q)

### Conservation et non conservation de l'énergie mécanique (en cours de rédaction)

Un exemple de réalisation utilisant un capteur analogique monté sur un pendule pesant associé à une `mesure temporelle lente`. Conforme au programme de la spécialité physique-chimie en première.

- le document utilisant `pduino` : [energie_mecanique.md](./docs/energie_mecanique/energie_mecanique.md) détaille le protocole de la manipulation et contient un exemple de TP testé en classe.
- en complément, si vous avez installé `juduino`, le document [...](...) détaille ces mesures effectuées sous Jupyter.
- un exemple de TP complet testé avec des élèves [...](...)


##### Vidéos de démonstration 

...
