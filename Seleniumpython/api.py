import requests
import pandas as pd

url = "https://flight-radar1.p.rapidapi.com/aircrafts/list"

headers = {
	"X-RapidAPI-Key": "0ebb338956msh171c0b762c43089p1e77b1jsncccae7c8b5a6",
	"X-RapidAPI-Host": "flight-radar1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
# df = pd.DataFrame(response)
# print(df)



print(response.json())