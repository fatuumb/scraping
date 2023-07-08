import json


with open('hotel_python.json', 'r') as json_file:
    data = json.load(json_file)


for item in data:
    if 'prix' in item and '\u00a0\u20ac' in item['prix']:

        price_str = item['prix'].replace('\u00a0\u20ac', '').replace(',', '')
        price_int = int(price_str)
        item['prix'] = price_int * 655
        item['note'] = float(item['note'].replace(',', '.')) 

with open('hotel_python_traite.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)