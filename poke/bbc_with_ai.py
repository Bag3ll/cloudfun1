import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text) ['results']
print(pokemon_list)

for pokemon in pokemon_list:
     print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)

if response.status_code != 200:
    print("Error: Pokémon not found.")
    exit()

pokemon_data = json.loads(response.text)

#ai pokemon code
ais_pokemon = random.choice(pokemon_list[:20])
ai_choice = ais_pokemon['name']

ai_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(ai_choice)
ai_response = requests.get(ai_url)
ai_pokemon_data = json.loads(ai_response.text)

print('Name: {}'.format(ai_pokemon_data['name']))

# Assign level 50
level = 50

# Fetch stats
stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
scaled_stats = {
    key: int((2 * value * level / 100) + level + 10 if key == 'hp' else (2 * value * level / 100) + 5)
    for key, value in stats.items()
}

# Get Pokémon types
types = [type_info['type']['name'] for type_info in pokemon_data['types']]

# Randomly select four moves
all_moves = [move['move']['name'] for move in pokemon_data['moves']]
if len(all_moves) < 4:
    print(f"{pokemon_data['name']} has fewer than 4 moves available.")
    moves = all_moves
else:
    moves = random.sample(all_moves, 4)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = pokemon_data['height'] / 10  # Convert decimetres to metres
weight = pokemon_data['weight'] / 10  # Convert hectograms to kilograms

# Assign level 50
ai_level = 50

# Fetch stats
ai_stats = {stat['stat']['name']: stat['base_stat'] for stat in ai_pokemon_data['stats']}
ai_scaled_stats = {
    key: int((2 * value * level / 100) + level + 10 if key == 'hp' else (2 * value * level / 100) + 5)
    for key, value in stats.items()
}

# Get Pokémon types
ai_types = [type_info['type']['name'] for type_info in ai_pokemon_data['types']]

# Randomly select four moves
ai_all_moves = [move['move']['name'] for move in ai_pokemon_data['moves']]
if len(ai_all_moves) < 4:
    print(f"{ai_pokemon_data['name']} has fewer than 4 moves available.")
    ai_moves = ai_all_moves
else:
    ai_moves = random.sample(ai_all_moves, 4)






# Print the pokemon's data
# print('Name: {}'.format(pokemon_data['name']))
# print('Weight: {}'.format(weight_formatted) + "(kgs)")
# print('Height: {}'.format(height_formatted) + "(m)")
# print('Ability: {}'.format(ability['name']))

# Print the Pokémon's data
print(f"\nPokémon: {pokemon_data['name'].capitalize()}")
print(f"Level: {level}")
print(f"Type: {', '.join(types).capitalize()}")
print(f"Height: {height} m")
print(f"Weight: {weight} kg")
print("Stats:")
for stat, value in scaled_stats.items():
    print(f"  {stat.capitalize()}: {value}")
print("Moves:")
for move in moves:
    print(f"  - {move.capitalize()}")


print(f"\nPokémon: {ai_pokemon_data['name'].capitalize()}")
print(f"Level: {ai_level}")
print(f"Type: {', '.join(types).capitalize()}")


print("Stats:")
for stat, value in ai_scaled_stats.items():
    print(f"  {stat.capitalize()}: {value}")
print("Moves:")
for move in ai_moves:
    print(f"  - {move.capitalize()}")