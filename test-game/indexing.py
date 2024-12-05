import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Fonction pour lire les documents texte dans un dossier
def read_documents(folder="processed_data"):
    documents = {}
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            documents[filename] = file.read()
    return documents

# Fonction pour construire l'index TF-IDF
def build_index(documents):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents.values())
    return vectorizer, tfidf_matrix

# Fonction pour sauvegarder l'index dans un fichier
def save_index(vectorizer, tfidf_matrix, index_file="index.pkl"):
    with open(index_file, "wb") as file:
        pickle.dump((vectorizer, tfidf_matrix), file)

# Fonction principale pour orchestrer le processus
if __name__ == "__main__":
    # Étape 1 : Lecture des documents
    print("Lecture des documents...")
    documents = read_documents()

    # Étape 2 : Construction de l'index
    print("Construction de l'index TF-IDF...")
    vectorizer, tfidf_matrix = build_index(documents)

    # Étape 3 : Sauvegarde de l'index
    print("Sauvegarde de l'index dans un fichier...")
    save_index(vectorizer, tfidf_matrix)
    print("Indexation terminée et sauvegardée sous 'index.pkl'.")
