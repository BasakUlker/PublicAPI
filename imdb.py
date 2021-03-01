import requests
import json

def returnBio(x):
    idx = x[0]
    for i in range(1,len(x)):
        idx = idx + x[i]
    url = "https://imdb8.p.rapidapi.com/actors/get-bio"

    querystring = {"nconst": idx}

    headers = {
        'x-rapidapi-key': "",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)
    print(result['name'])
    return 0

month = int(input("Kacinci ay: "))
day = int(input("Kacinci gün: "))

url = "https://imdb8.p.rapidapi.com/actors/list-born-today"

querystring = {"month": month,"day": day}

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
result = json.loads(response.text)
print(month, ". ay",day,". gun dogan unluler: ")
for i in range(0,len(result)):
    arr = list(result[i])
    returnBio(arr[6:15])
print("Done.")
#print(json.dumps(result,indent = "\n", sort_keys = True))

