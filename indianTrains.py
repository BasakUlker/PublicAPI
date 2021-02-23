import requests
import json

url = "https://trains.p.rapidapi.com/"

payload = {
	"content-type": "application/json",
	"x-rapidapi-key": "",
	"x-rapidapi-host": "trains.p.rapidapi.com",
}

headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "",
    'x-rapidapi-host': "trains.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, data = payload)
print(response.text)
