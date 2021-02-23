import requests
import json

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"eminem"}

headers = {

        "x-rapidapi-key":"12f443f6f9msh31241e38a337832p1c38aajsn6fe394aeeb79",
        "x-rapidapi-host": "deezerdevs-deezer.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params = querystring)
result = json.loads(response.text)
print(result)



