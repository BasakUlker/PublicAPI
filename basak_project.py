import requests
from requests.exceptions import HTTPError
ad = input("Please, paste your http address: ")
#req = requests.get(ad)
#print(req)
#print(req.encoding)
#print(req.status_code)


while(1==1):

    print("Please, choose one of requests in below and type the number:\n1-POST\n2-PUT\n3-DELETE\n4-HEAD\n5-PATCH\n6-OPTIONS\n7-GET\n0-EXIT")
    x = int(input("Number:"))

    if(x == 1):

        adpost1 = requests.post(ad)
        key = input("A key for POST option: ")
        value = input("A value for POST option: ")

        adpost = requests.post(ad, data = {key:value})
        print(adpost)
        if(adpost1 != adpost):
            print("Succeed!")
        else:
            print(f'HTTP error occurred: {http_err}')

    if(x == 2):

        adput1 = requests.put(ad)

        key = input("A key for PUT option: ")
        value = input("A value for PUT option: ")

        adput = requests.put(ad, data = {key:value})
        print(adput)
        if(adput1 != adput):
            print("Succeed!")
        else:
            print(f'HTTP error occurred: {http_err}')

    if(x == 3):

        addel = requests.delete(ad)


    if(x == 4):

        adhead = requests.head(ad)

        print(adhead)

    if(x == 5):

        adpatch1 = requests.patch(ad)

        key = input("A key for PATCH option: ")
        value = input("A value for PATCH option: ")

        adpatch = requests.patch(ad, data ={key:value})
        print(adpatch)

        if(adpatch1 != adpatch):

            print("Succeed!")
        else:
            print(f'HTTP error occurred: {http_err}')


    if(x == 6):

        adoptions = requests.options(ad)
        print(adoptions)
    
    if(x == 7):

        adget = requests.get(ad)
        print(adget)


    if(x == 0):

        break

