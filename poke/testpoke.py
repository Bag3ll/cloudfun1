import requests
import random

# Function to fetch data from the API
def fetch_data(datas):
    response = requests.get(datas)
    if response.status_code != 200:
        print("Error: Unable to fetch data.")
        exit()
    return response.json()

# Get the full list of Pokémon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
pokemon_list = []
while url:
    data = fetch_data(url)
    pokemon_list.extend(data['results'])
    url = data.get('next')  # Pagination

# Display Pokémon names
print("Available Pokémon:")
for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a Pokémon
choice = input('Enter your Pokémon: ').strip().lower()

# Validate the choice
if not any(pokemon['name'] == choice for pokemon in pokemon_list):
    print('Invalid Pokémon name. Please try again.')
    exit()

# Fetch Pokémon details
url = f'https://pokeapi.co/api/v2/pokemon/{choice}/'
pokemon_data = fetch_data(url)

# Assign level 50
level = 50

# Fetch stats
stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
# Calculate scaled stats (rough estimation formula)
scaled_stats = {
    key: int((2 * value * level / 100) + level + 10 if key == 'hp' else (2 * value * level / 100) + 5)
    for key, value in stats.items()
}

# Randomly select four moves
all_moves = [move['move']['name'] for move in pokemon_data['moves']]
if len(all_moves) < 4:
    print(f"{pokemon_data['name']} has fewer than 4 moves available.")
    moves = all_moves
else:
    moves = random.sample(all_moves, 4)

# Get Pokémon types
types = [type_info['type']['name'] for type_info in pokemon_data['types']]

# Display the Pokémon's details
print(f"\nPokémon: {pokemon_data['name'].capitalize()}")
print(f"Level: {level}")
print(f"Type: {', '.join(types).capitalize()}")
print("Stats:")
for stat, value in scaled_stats.items():
    print(f"  {stat.capitalize()}: {value}")
print("Moves:")
for move in moves:
    print(f"  - {move.capitalize()}")
