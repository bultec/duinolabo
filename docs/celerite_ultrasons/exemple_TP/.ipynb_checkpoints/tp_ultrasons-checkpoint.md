# Célérité des ultrasons et radar de recul

La maquette utilisée est la suivante

![](data/image_3.jpeg)


## I. Questions préliminaires
- Schématisez la situation en faisant apparaitre la progression des ondes ultrasonores depuis l'émetteur jusqu’au récepteur.
- La voiture se trouve à 1,70 m d’un obstacle. Montrez que la distance parcourue par l’onde ultrasonore après un aller-retour est de 3,40 m lorsque l'écho revient au pare-choc.

## II. Détermination de la vitesse des ultrasons dans l’air.
### 1. Dispositif
Réaliser le montage suivant
 
![](data/image_16.png) 
 
### 2.Mesures
- Réaliser le montage ci-dessus.
- Ouvrir le fichier `capteur_us.ino` dans le logiciel Arduino.
- Sélectionner le port `COM` et téléverser le programme dans la carte.
- Ouvrir le fichier python `ultrasons_mesures.py`, renseigner le port `COM` et exécuter le programme.
- Placer la maquette de telle façon que le capteur à ultrasons soit situé à une distance $d=10,0~cm$ de l'obstacle et effectuer la mesure de la durée $\Delta t$ du parcours aller retour de l’onde ultrasonore.
- Renouveler l’opération pour des valeurs de $d$ comprises entre 10,0 cm et 80 cm par pas de 5,0 cm. Cliquer sur `Cancel` pour terminer.
- Si les mesures vous conviennent, fermer la fenêtre graphique et taper `mesures` comme nom du fichier dans la boite de dialogue. Un fichier `mesures.csv `est enregistré. Il contient le tableau des valeurs de $d$ et $\Delta t$.

### 3. Evaluation des incertitudes et saisie des mesures
On utilisera le fichier `celerite_ultrasons.py`.
En observant votre matériel, évaluer l'incertitude absolue $\Delta D$ sur la mesure de la distance $d$.

Le constructeur indique que l'incertitude sur la mesure de $\Delta t$ est de l’ordre de 100µs.

- Compléter la partie `# lecture du fichier de mesures et évaluation des incertitudes`  de façon à convertir vos données dans les bonnes unités.

- Saisir les valeurs des incertitudes en complétant les lignes :
```python
    # incertitudes sur d
    d_ErrorValues = np.array([... for valeur in d])
    # incertitudes sur t
    t_ErrorValues = np.array([... for valeur in t])
```

### 4. Graphe $t = f(d)$
Compléter les lignes 
```python
plt.xlabel('...',fontsize = 18)         # Label de l'axe des abscisses
plt.ylabel('...',fontsize = 18)         # Label de l'axe des ordonnées
plt.plot(..., ..., 'r.', ms=8, label='Points expérimentaux') # Points expérimentaux
```
de façon à obtenir le graphe $\Delta t = f(d)$ ainsi que sa modélisation.

Evaluer la qualité de vos mesures. Appelez le professeur.

### 5. Détermination de la célérité des ultrasons dans l’air
Soit $V_{son}$ la célérité de l’onde sonore.

- Etablir la relation existante entre les grandeurs $d$, $\Delta t$ et $V_{son}$ .

- A partir de la relation précédente et du coefficient directeur $m$ de la droite obtenue, déterminer la célérité des ultrasons dans l'air de la pièce.

- Pour une température de 20°C, une pression de 1013hPa et une humidité relative nulle, la célérité de la propagation d'une l'onde sonore dans l'air est d'environ $343~m.s^{-1}$. Evaluer l’incertitude relative $\frac {\Delta V_{son}}{V_{son}}$ sur la mesure de $V_{son}$..


## III. Application au radar de recul
### 1. Un peu de langage C
Pour allumer une led sur la maquette, il faudra utiliser l'instruction 

```c
digitalWrite(pin_led, HIGH);
```
et pour l’éteindre
```c
digitalWrite(pin_led, LOW);
```

Pour attendre x millisecondes, il faudra utiliser l’instruction
```c
delay(x);
```

### 2. Réalisation d’un radar de recul
On souhaite utiliser la maquette pour fabriquer un radar de recul. Le cahier des charges est le suivant :

- Lorsque le radar est situé à plus d’un mètre de l'obstacle :
    - la del verte doit être allumée et la del rouge doit être éteinte
    - le buzzer ne doit émettre aucun son

<p></p>

- Lorsque le radar est situé entre 50 cm et 1,00 m de l'obstacle :
    - la del verte doit être allumée et la del rouge doit être éteinte
    - le buzzer doit émettre un bip toutes les 300 ms

<p></p>

- Lorsque le radar est situé à moins de 50 cm de l'obstacle :
    - la del verte doit être éteinte et la del rouge doit être allumée
    - le buzzer doit émettre un bip toutes les 125 ms

Compléter le programme [programme_2.ino](programme_2.ino) de façon à répondre au cahier des charges puis téléverser le sur la maquette.
