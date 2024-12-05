import requests
import os

# Clé API RAWG.io
API_KEY = "e65be5f978db4dedb058d142d9317f48"
BASE_URL = "https://api.rawg.io/api"

def fetch_games(page_size=20, num_pages=1):
    games = []
    for page in range(1, num_pages + 1):
        params = {"key": API_KEY, "page_size": page_size, "page": page}
        response = requests.get(f"{BASE_URL}/games", params=params)
        if response.status_code == 200:
            games.extend(response.json()["results"])
        else:
            print(f"Erreur {response.status_code}: Impossible de récupérer les données.")
    return games

def save_to_text_files(games, folder="games_data"):
    os.makedirs(folder, exist_ok=True)
    for game in games:
        file_path = os.path.join(folder, f"{game['id']}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"Title: {game['name']}\n")
            file.write(f"Description: {game.get('description_raw', 'N/A')}\n")
            file.write(f"Genres: {', '.join([genre['name'] for genre in game['genres']])}\n")
            file.write(f"Released: {game['released']}\n")

if __name__ == "__main__":
    print("Fetching games...")
    games = fetch_games(page_size=5, num_pages=2)  # Récupère 10 jeux
    print(f"Nombre de jeux récupérés : {len(games)}")
    print("Saving games to text files...")
    save_to_text_files(games)
    print("Terminé.")
