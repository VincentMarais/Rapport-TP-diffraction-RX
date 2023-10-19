import numpy as np
import matplotlib.pyplot as plt

# Données
theta_degrees = np.array([0.238, 0.277, 0.396, 0.469, 0.492, 0.492, 0.645, 0.658, 0.730])
delta_theta_degrees = np.array([0.02, 0.02, 0.01, 0.009, 0.009, 0.008, 0.007, 0.007, 0.006])
d_hkl = np.array([3.252, 2.811, 1.992, 1.699, 1.627, 1.408, 1.280, 1.258, 1.153])
delta_d_hkl = np.array([0.02, 0.02, 0.01, 0.009, 0.008, 0.007, 0.006, 0.006, 0.005])

# Convertir les angles de degrés en radians
theta_radians = np.deg2rad(theta_degrees)
delta_theta_radians = np.deg2rad(delta_theta_degrees)

# Calculer sin(theta) et delta(sin(theta))
sin_theta = np.sin(theta_radians)
delta_sin_theta = np.abs(np.cos(theta_radians) * delta_theta_radians)

# Régression linéaire
coefficients = np.polyfit(sin_theta, d_hkl, 1)
a, b = coefficients

# Créer une figure
plt.figure(figsize=(8, 6))

# Tracer d_{hkl} en fonction de sin(theta) avec des barres d'erreur rouges
plt.errorbar(sin_theta, d_hkl, xerr=delta_sin_theta, yerr=delta_d_hkl, fmt='o', markersize=5, capsize=3, color='black', label='Données expérimentales')

# Tracer de la courbe de tendance
trend_line = a * sin_theta + b
plt.plot(sin_theta, trend_line, label=f'Courbe de tendance: $d = {a:.4f} \sin(\\theta) + {b:.4f}$')

# Titres et labels des axes
plt.title('Relation entre $d_{hkl}$ et $sin(\\theta)$ avec Courbe de tendance')
plt.xlabel('$sin(\\theta)$')
plt.ylabel('$d_{hkl}$ (\AA)')

# Afficher la légende
plt.legend()

# Afficher le graphique
plt.grid(True)
plt.show()
