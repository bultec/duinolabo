#### Thème 2: Mouvement et interaction - Description d'un fluide au repos

# Vérifier la loi de Mariotte

## Fiche élève

## Problématique

Quel est le comportement d'un gaz lorsque sa pression ou son volume varient ?

## Objectifs 

- Effectuer des mesures de volume et de pression pour vérifier la loi de Mariotte.
- Valider les résultats en réalisant une modélisation numérique.

<div class="alert alert-success">

### Compétences

#####  Analyser/Raisonner

- Formuler des hypothèses.
- Choisir un modèle ou des lois pertinentes.
- Choisir, élaborer, justifier un protocole.
- Faire des prévisions à l'aide d'un modèle.

#### Réaliser

- Mettre en œuvre les étapes d'une démarche.
- Utiliser un modèle.
- Effectuer des procédures courantes (calculs, représentations, collectes de données, etc.)
- Faire preuve d'esprit critique, procéder à des tests de vraisemblance.

#### Valider
- Confronter un modèle à des résultats expérimentaux.
</div>

## Matériel :
Valise *Arduino* contenant :
- Une carte Arduino + capteurs *Groove*
- Un capteur de pression
- Une seringue munie d'un tube souple
- Ordinateur muni du logiciel _Arduino_ et du langage Python avec la bibliothèque _pyduino_ installée.


<div class="alert alert-info">

### Document 1 : la loi de Mariotte
    
Les gaz sont compressibles, c 'est-à-dire que le volume d'une quantité de matière de gaz donnée varie quand sa pression varie.

**Unités**                                                              
- Unité de pression : le pascal (Pa) : $1~hPA = 1 \times 10^2~Pa$
- Unité de volume : le mètre cube ($m^3$) : $1~mL = 1~cm^3 = 1 \times 10^{-6}~m^3$
</div>

<div class="alert alert-danger">

Notre objectif : établir la loi qui relie la pression et le volume d'un gaz.
</div>

### Document 2 : rappel mathématique

La proportionnalité entre deux grandeurs $x$ et $y$ est traduite par une fonction linéaire du type $y = a\times x$.

La représentation graphique d'une telle fonction est une droite passant par l'origine.

![](data/image_1.svg)
    
Le coefficient directeur de la droite est :
$$a = \frac{y_B-y_A}{x_B-x_A}
$$

### Document 3 : mise en fonction du capteur de pression

- Relier un capteur de pression à l'entrée analogique `A0` d'une carte _Arduino_.

![](data/image_1.png)
- Connecter la carte sur le port USB de l'ordinateur et lancer le logiciel
_Arduino_.
- Ouvrir le programme `capteur_pression.ino`.
- Sélectionner le port sur lequel est branchée la carte _Arduino_ et noter la valeur de ce port.
- Téléverser le programme dans la carte.
- Fermer le logiciel _Arduino_.
- Déplacer le piston de la seringue de façon à emprisonner un volume $V=60~mL$ d'air dans la seringue et relier le tuyau au capteur.

![](data/image_2.png)

- Ouvrir le programme `test_pression.py` à l'aide du logiciel _edupython_.

Modifier la ligne :
```python
port = 'COM8'
```
en remplaçant _COM8_ par le port sur lequel est relié la carte _Arduino_ (noté précédemment).



### Document 4 : étalonnage du capteur
- Exécuter le programme : ce dernier affiche la pression (en hPa) àl'intérieur de la seringue, soit, au début de l'expérience, la pression atmosphérique $P_0$.
- Relever la pression atmosphérique locale sur internet.
- Modifier par tâtonnement la valeur du coefficient `k` de façon à ce que le
capteur affiche la valeur de la pression atmosphérique relevée précedemment.
- Noter la valeur de `k`.

## Démarche d'investigation

### Préparation du programme

Ouvrir le programme  `mariotte_mesure.py`  à l'aide du logiciel _edupython_.

Modifier la valeur du port _COM_, ainsi que la valeur du coefficient `k` en fonction des valeurs notées précédemment.

### Protocole

- Exécuter le programme `mariotte_mesure.py` 
- Effectuer la première mesure de pression pour un volume d'air contenu dans la seringue $V=60~mL$
-  Appuyer doucement sur le piston et renouveler 9 fois la mesure pour des volumes régulièrement espacés compris entre 60 mL et 20 mL.
- Sauvegardez le fichier sous le nom de votre choix.

### Exploitation

- Exécuter le programme `loi_mariotte_resultats.py` 
- Compléter la ligne 
```python
V, P = np.array(lit_fichier('---.csv'))
```
avec le nom de fichier choisi dans le paragraphe précédent.
- De façon à travailler dans le S.I. compléter les lignes :

```python
V = V * ...
P = P * ...
```

De façon à calculer l'inverse du volume compléter la ligne :

```python
inv_V = ...
```

## Questions
1. Quelle droite a-t-on tracé ?
2. Quel est le coefficient directeur `m` de cette droite ?
3. Écrire la relation entre `P`, `V` et `m`. En déduire la loi de Mariotte.

Une constante apparaît dans cette loi. Exprimer cette constante en fonction de $P_0$ et de $V_0$ et préciser son unité.

## Pour aller plus loin

A l'aide du programme `test_pression.py`, en gardant le piston de la seringue immobile, poser la paume de la main sur le cylindre pour chauffer l'air qu'il contient. Observer comment évolue la pression.

**Conclusion**

L'expérience décrite au paragraphe précédent prouve que la constante dépend d'un paramètre au moins. Lequel ?
