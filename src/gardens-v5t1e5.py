import itertools
import json
import random

copy_garden_names = {
    'Strathcona Community Garden',
    'Cottonwood Community Garden',
    'Elisabeth Rogers Community Garden',
    'City Hall Lawn Garden',
    'City Hall expansion',
    'Village on False Creek',
    'China Creek Community Garden',
    'China Creek North Park',
    'China Creek Housing Co-op',
    'Cedar Cottage Community Garden',
    'Cedar Cottage Community Garden - Part 2'
}

data = json.load(open('gardens.json'))
copied_data = []
for row in data:
    if row.get('NAME') in copy_garden_names:
        copied_data.append(row)

json.dump(copied_data, open('gardens-v5t1e5.json', 'w'), indent=4)
