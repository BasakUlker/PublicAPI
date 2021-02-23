import requests
import json

url = "https://trains.p.rapidapi.com/"

payload = {
	"content-type": "application/json",
	"x-rapidapi-key": "12f443f6f9msh31241e38a337832p1c38aajsn6fe394aeeb79",
	"x-rapidapi-host": "trains.p.rapidapi.com",
}

headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "12f443f6f9msh31241e38a337832p1c38aajsn6fe394aeeb79",
    'x-rapidapi-host': "trains.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, data = payload)
print(response.text)
