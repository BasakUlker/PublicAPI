#This program is listing most popular movies.

import requests
import json

def returnTitle(x):

    tx = x[0]
    for i in range(1,len(x)):
        tx = tx + x[i]
    url = "https://imdb8.p.rapidapi.com/title/get-plots"

    querystring = {"tconst": tx}

    headers = {
        'x-rapidapi-key': "",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)
    print(result["base"]["title"])
    return 0

url = "https://imdb8.p.rapidapi.com/title/get-popular-movies-by-genre"

querystring = {"genre":"/chart/popular/genre/adventure"}

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
result = json.loads(response.text)
#print(json.dumps(result,indent = "\n", sort_keys = True))
for i in range(0, len(result)):
    arr = list(result[i])
    q = len(arr)-1
    returnTitle(arr[7:q])

