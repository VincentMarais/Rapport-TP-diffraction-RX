import math

# Données
donnees = [
    (1, 27.4, 0.238, 0.02, 57.35),
    (2, 31.8, 0.277, 0.02, 57.35),
    (3, 45.5, 0.396, 0.01, 57.35),
    (4, 53.9, 0.469, 0.009, 57.35),
    (5, 56.5, 0.492, 0.009, 57.35),
    (6, 66.3, 0.492, 0.008, 57.35),
    (7, 74.0, 0.645, 0.007, 57.35),
    (8, 75.5, 0.658, 0.007, 57.35),
    (9, 83.8, 0.730, 0.006, 57.35)
]

raie = [row[0] for row in donnees]
phi_an = [row[1] for row in donnees]
theta = [row[2] for row in donnees]
delta_theta = 0.004
phi_DS = [row[4] for row in donnees]
print(phi_an)
print(phi_DS)
delta_phi_an = 0.5
delta_phi_DS = 0.002    
lambda_raie = 1.539
delta_lambda = 0.001
# Calcul pour chaque donnée
resultats = []
delta_d_hkl_s = []

for i in range(len(donnees)):
    phi_DS_val = phi_DS[i]
    phi_an_val = phi_an[i]
    theta_val = theta[i]         

    resultat = math.sqrt(
        (delta_phi_an / (2 * phi_DS_val))** 2 +
        (((delta_phi_DS  * phi_an_val) / (2 * phi_DS_val ** 2)) ** 2)
    )
    resultats.append(resultat)

    delta_d_hkl = math.sqrt(
        ((delta_lambda / 2*(math.sin(theta_val))) ** 2) + 
        (((delta_theta * lambda_raie) / (2 * math.tan(theta_val)*math.sin(theta_val))) ** 2)
    )
    delta_d_hkl_s.append(delta_d_hkl)

# Affichage des résultats
for i, resultat in enumerate(resultats):
    print(f"Résultat pour la donnée {i+1} :", resultat)

for i, delta_d_hkl in enumerate(delta_d_hkl_s):
    print(f"Résultat pour la d_hkl {i+1} :", delta_d_hkl)
