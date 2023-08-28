#!/usr/bin/env python
# coding: utf-8

# Célérité des ultrasons dans l'air

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import matplotlib.ticker as ticker
from pduino import *

# #### lecture du fichier de mesures et évaluation des incertitudes
d, dt = np.array(lit_fichier('mesures_us.csv'))
# distance aller retour (m)
d = d * 1e-2
# durée aller retour (s)
dt = dt * 1e-6
# incertitudes sur d
d_ErrorValues = np.array([1.0e-2 for valeur in d])
# incertitudes sur t
t_ErrorValues = np.array([100e-6 for valeur in dt])

# #### Paramétrage du graphique et choix des grandeurs placées en abscisse et en ordonnée
# calcul du modèle
Modele = linregress(d,dt)
m, p = Modele[0],Modele[1]
plt.figure("Célérité des ultrasons",figsize=(11,8))# Initialise la figure
plt.title("Célérité des ultrasons dans l'air",fontsize = 20)# Titre du graphe
plt.xlabel('$d (m)$',fontsize = 18)         # Label de l’axe des abscisses
plt.ylabel('$\Delta t (s)$',fontsize = 18)         # Label de l’axe des ordonnées
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2f'))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2e'))
plt.xticks(fontsize=14)
plt.ticklabel_format(axis='x')
plt.ticklabel_format(axis='y')
plt.yticks(fontsize=14)
plt.plot(d, dt, 'r.', ms=8, label='Points expérimentaux') # Points expérimentaux
plt.plot(d, m*d+p, 'b--', label='Régression linéaire', lw=1)
plt.errorbar(d, dt, xerr = d_ErrorValues, yerr = t_ErrorValues, fmt = 'none', capsize = 2, ecolor = 'green', zorder = 1)
plt.grid()
plt.legend(fontsize=14)
print('Modélisation de la droite : dt = m x d avec m = {:.2e} s/m'.format(m))
plt.show()

