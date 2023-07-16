#!/usr/bin/env python
# coding: utf-8

# # Loi de Mariotte

# Importation des biblothèques
import time
import matplotlib.pyplot as plt     # Importe le module pyplot en plt
import matplotlib
import numpy as np                  # Importe la bibliothèque numpy en np
from scipy.stats import linregress

# initialisation
#plt.rc('text',usetex=True)
#matplotlib.rcParams['text.usetex'] = True

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pyduino import lit_fichier

# Lit le fichier de mesures et le stocke dans des tableaux
V, P = np.array(lit_fichier('mesures_P.csv'))

# V est donné el mL. On le convertit en m3
V = V * 1e-6
# P en donnée en hPa. On la convertit en Pa
P = P * 1e2
# on calciule l'inverse de V
inv_V = 1/V

# Calcul du modèle linéaire de la forme 𝑦 = m × 𝑥 + p
Modele = linregress(inv_V, P) # calcul du modèle
m, p = Modele[0], Modele[1]

# Affichage en mode texte
print('Modélisation de la courbe :')
print('m =','{:.2f}'.format(m),'Pa.L')

# Paramétrage du graphique et choix des grandeurs placées en abscisse et en ordonnée
plt.figure('Loi de Mariotte', figsize=(10, 7))# Initialise la figure
plt.title('Loi de Mariotte', fontsize = 18)  # Titre du graphe
plt.xlabel('1/V (m-3)', fontsize = 16)             # Label de l’axe des abscisses
plt.ylabel('P (Pa)', fontsize = 16)         # Label de l’axe des ordonnées
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks(fontsize=14)
plt.ticklabel_format(axis='x', style='scientific', scilimits=(-1,2))
plt.ticklabel_format(axis='y', style='scientific', scilimits=(-1,2))
plt.yticks(fontsize=14)
plt.plot(inv_V, P, 'r+', ms=14, label='Points expérimentaux') # Points expérimentaux
plt.plot(inv_V, m*inv_V+p, 'b--', label='Régression linéaire', lw=1)
plt.grid()                                            # Affiche une grille
plt.legend(fontsize=14)
plt.show()



