import pickle

# Charger le fichier index.pkl
with open("index.pkl", "rb") as file:
    index = pickle.load(file)

# Afficher le contenu pour comprendre la structure
print("Type de données :", type(index))
print("Aperçu du contenu :", index)

# Si c'est un dictionnaire, afficher les clés principales
if isinstance(index, dict):
    print("Clés principales :", list(index.keys())[:10])
