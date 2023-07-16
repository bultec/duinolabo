import matplotlib.pyplot as plt
from pyduino import lit_fichier
import numpy as np

def recherche_front_montant(t, E):
    for i in range(len(E)-1):
        if (int(E[i+1]) == 1 ) and (int(E[i]) == 0 ):
            m_t = (t[i] + t[i+1]) / 2
            return m_t
    return None

def recherche_front_descendant(t, E):
    for i in range(len(E)-1):
        if (int(E[i+1]) == 0 ) and (int(E[i]) == 1 ):
            m_t = (t[i] + t[i+1]) / 2
            return m_t
    return None


# --- Lit le fichier de mesures
t, E = np.array(lit_fichier('sauve_us.csv'))

# --- calcul de la célérité du son ---
d = 40e-2
t1 = recherche_front_montant(t, E)
t2 = recherche_front_descendant(t, E)
dt =  t2 - t1
v = 2 * d / dt
print('Célérité des ultrasons dans l\'air : V = {} m.s-1'.format(round(v, 1)))

# --- affiche le graphique
fig_c = plt.figure("Célérité des ultrasons", figsize=(6, 4))
plt.title("Célérité des ultrasons dans l'air")
plt.plot(t*1000, E, marker = '*', label = 'E')
plt.grid()
plt.xlabel('t (ms)')
plt.ylabel ('E (sans unité)')
plt.legend()
plt.show()