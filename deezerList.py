import requests
import json

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"eminem"}

headers = {

        "x-rapidapi-key":"",
        "x-rapidapi-host": "deezerdevs-deezer.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params = querystring)
result = json.loads(response.text)
print(result)



