import requests
import json
import random


#assign level to pokemon (50)
#get move
#take its power


# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text) ['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

#moves = pokemon_data['moves']
#for move in moves:
#    print(move['move'])

#moves_api = requests.get('https://pokeapi.co/api/v2/move/5/')
#moves_json = json.loads(moves_api.text)
#print(moves_json)

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])
height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))



#ai pokemon code
ais_pokemon = random.choice(pokemon_list[:20])
ai_choice = ais_pokemon['name']

print(ais_pokemon)
ai_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(ai_choice)
ai_response = requests.get(ai_url)
ai_pokemon_data = json.loads(ai_response.text)

print('Name: {}'.format(ai_pokemon_data['name']))


