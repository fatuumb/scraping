import json


with open('hotel_js.json', 'r') as json_file:
    data = json.load(json_file)

for item in data:
    if 'prix' in item and item['prix'].startswith('XOF '):
        item['prix'] = int(item['prix'][4:].replace(',', '') )

with open('hotel_js_traite.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)
