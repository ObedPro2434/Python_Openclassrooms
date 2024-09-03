# 1. Création d'une liste de fruits
fruits = ["pomme", "banane", "orange"]
print(fruits)

# 2. Ajout d'autres fruits 
fruits.append("kiwi")
print(fruits)

# 3. Suppression de orange de la liste fruits
fruits.remove("orange")
print(fruits)

# 4. Changement du deuxième éléments par ananas
fruits[1] = "ananas"

# 5. longueur de la liste fruits
nb = len(fruits)
print(f"La liste de fruits contient {nb} fruits.")

# 6. triage par odre alphabetique
fruits.sort()
print(fruits)
