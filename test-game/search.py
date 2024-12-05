import pickle
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import string

def preprocess_query(query):
    nltk.download('punkt')
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(query.lower())
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return " ".join(tokens)

def search(query, index_file="index.pkl", top_n=5):
    # Charger l'index (vecteur TF-IDF et matrice)
    with open(index_file, "rb") as file:
        vectorizer, tfidf_matrix = pickle.load(file)

    # Prétraitement de la requête
    query = preprocess_query(query)

    # Transformer la requête en vecteur TF-IDF
    query_vector = vectorizer.transform([query])

    # Calculer la similarité cosinus entre la requête et les documents
    similarities = cosine_similarity(query_vector, tfidf_matrix)

    # Obtenir les indices des documents les plus pertinents
    top_indices = similarities.argsort()[0][-top_n:][::-1]

    # Résultats
    results = []
    for idx in top_indices:
        score = similarities[0, idx]
        if score > 0.1:  # Seuil de pertinence
            results.append((idx, score))
    
    return results

if __name__ == "__main__":
    query = input("Entrez votre requête : ")
    results = search(query)
    print("Résultats les plus pertinents :")
    for doc_id, score in results:
        print(f"Document ID : {doc_id}, Score : {score}")
