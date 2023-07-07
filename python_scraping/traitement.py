import json


with open('data.json', 'r') as json_file:
    data = json.load(json_file)


for item in data:
    if 'prix' in item and '$' in item['prix']:

        price_str = item['prix'].replace('$' , '').replace(',', 'fr')
        price_int = int(price_str)
        item['prix'] = price_int * 655

with open('data_traite.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)