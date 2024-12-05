import nltk
nltk.download('punkt', download_dir='C:\\Users\\pc\\AppData\\Roaming\\nltk_data')
nltk.download('punkt_tab', download_dir='C:\\Users\\pc\\AppData\\Roaming\\nltk_data')
nltk.download('punkt', download_dir='C:\\Users\\pc\\AppData\\Roaming\\nltk_data')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
text = "Voici un exemple de texte."
tokens = word_tokenize(text)
print(tokens)
