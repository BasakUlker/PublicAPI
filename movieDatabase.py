import requests
import json

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

payload = {

	"s": "Avengers Endgame",
	"page": "1",
	"r": "json"
} 

headers = {
	"x-rapidapi-key": "12f443f6f9msh31241e38a337832p1c38aajsn6fe394aeeb79",
	"x-rapidapi-host": "movie-database-imdb-alternative.p.rapidapi.com",
}

response = requests.request("GET", url, headers=headers, data = payload)
result = json.loads(response.text)
print(result)
