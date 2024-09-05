# 1. Création du dictionnaire
fruits = {"pomme": "rouge", "banane": "jaune", "orange": "orange"}
print(fruits)

# 2. Ajout d'element
fruits["kiwi"] = "vert"
print(fruits)

# 3. Acceder à une valeur
couleur_banane = fruits.get("banane")
print(couleur_banane)

# 4. Modification d'une valeur 
fruits["pomme"] = "vert"
print(fruits)

# 5. Suppression d'élément
del fruits["banane"]
print(fruits)

# 6. Affichage de éléments restants
rest_keys = fruits.keys()
print("Les clés restantes du dictionnaire de fruits est",rest_keys)
