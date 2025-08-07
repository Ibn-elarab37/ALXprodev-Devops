#!/usr/bin/env python3

import requests
import os
import time

# Create output directory if not exists
os.makedirs("pokemon_data", exist_ok=True)

pokemon_list = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon"]

for name in pokemon_list:
    lower_name = name.lower()
    print(f"Fetching data for {lower_name}...")

    url = f"https://pokeapi.co/api/v2/pokemon/{lower_name}"
    response = requests.get(url)

    if response.status_code == 200:
        with open(f"pokemon_data/{lower_name}.json", "w") as f:
            f.write(response.text)
        print(f"Saved data to pokemon_data/{lower_name}.json ✅")
    else:
        print(f"Failed to fetch data for {lower_name} ❌")

    time.sleep(1)

