import requests
import random

def fetch_characters():
    url = "https://hp-api.onrender.com/api/characters"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def show_random_characters(n=3):
    characters = fetch_characters()
    selection = random.sample(characters, n)
    for char in selection:
        print(f"Name:   {char.get('name', 'Unknown')}")
        print(f"House:  {char.get('house', 'Unknown')}")
        print('-' * 30)


print("✨ Random Harry Potter Characters:")
show_random_characters(5)
print("✨ Enjoy the magic! ✨")