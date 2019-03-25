import itertools
import json
import random

types = ['Neighbourhood', 'Youth', '']
# food_grown = ['Apples', 'Potatoes', 'Apples, Potatoes']

def get_random_status():
   options = list(itertools.repeat('Waitlist ({})'.format(random.randint(10, 100)), times=9))
   options.append('Open')
   return random.choice(options)

data = json.load(open('gardens.json'))
for row in data:
    if 'GARDEN_TYPE' not in row:
        row['GARDEN_TYPE'] = random.choice(types)

    # if 'FOOD_GROWN' not in row:
    #     row['FOOD_GROWN'] = random.choice(food_grown).join(', ')

    if 'REGISTRATION_STATUS' not in row:
        row['REGISTRATION_STATUS'] = get_random_status()

    row['ACTIONS'] = ''

json.dump(data, open('gardens.json', 'w'), indent=4)
