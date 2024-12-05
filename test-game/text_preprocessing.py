import os
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('punkt')
nltk.download('wordnet')

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(lemmatized_tokens)

def preprocess_files(input_folder="games_data", output_folder="processed_data"):
    os.makedirs(output_folder, exist_ok=True)
    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)
        with open(input_path, "r", encoding="utf-8") as infile:
            content = infile.read()
        preprocessed_content = preprocess_text(content)
        with open(output_path, "w", encoding="utf-8") as outfile:
            outfile.write(preprocessed_content)

if __name__ == "__main__":
    preprocess_files()

test_text = "The quick brown FOXES jump over the lazy DOGS during summer nights!"
print(preprocess_text(test_text))
#output:the quick brown fox jump over the lazy dog during summer night !