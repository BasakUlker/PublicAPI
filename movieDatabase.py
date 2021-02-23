import requests
import json

url = "https://imdb8.p.rapidapi.com/actors/list-born-today"

querystring = {"month":"7","day":"27"}

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params = querystring)
result = json.loads(response.text)
print(result)

