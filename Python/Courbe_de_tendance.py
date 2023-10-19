import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Les données
sin_theta = np.array([0.111, 0.125, 0.223, 0.25, 0.335, 0.376])
n_lambda = np.array([63.2, 70.9, 126.4, 141.8, 189.6, 212.7])

# Créer un modèle de régression linéaire
coefficients = np.polyfit(sin_theta, n_lambda, 1) # 1 pour une régression linéaire (premier degré)
polynome = np.poly1d(coefficients)

# Calculer les nouvelles valeurs de y
y_new = polynome(sin_theta)

# Calculer R^2
r2 = r2_score(n_lambda, y_new)

# Créer la courbe de tendance
plt.scatter(sin_theta, n_lambda, color='red', label='Données')
plt.plot(sin_theta, y_new, color='forestgreen', label=r'$f\left ( \sin \left ( \theta \right ) \right )$')
plt.xlabel(r'$\sin(\theta)$')
plt.ylabel(r'$n \times \lambda$ (pm)')

# Position personnalisée pour le texte
pos_x = sin_theta.min() + (sin_theta.max() - sin_theta.min()) * 0.2  # par exemple, 10% de la largeur du graphique à partir du min
pos_y = n_lambda.max() - (n_lambda.max() - n_lambda.min()) * 0.2 # par exemple, 10% de la hauteur du graphique à partir du max

plt.text(pos_x ,pos_y, f'Équation: {polynome}\n$R^2$: {r2}', fontsize=12) # Affiche l'équation et R^2 sur le graphique
plt.legend()
plt.show()