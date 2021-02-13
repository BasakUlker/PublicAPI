import requests
import ipaddress
import re
from requests.exceptions import HTTPError

while(1==1):

    x=0 
    ad = input("Please, paste your http address: ")

    
   # a = {"h","t","p","s"}
    #b = list(ad)
    #c = set(b[:4])
   # inter = a.intersection(c)
    #if(len(inter)!=3):

     #   ad = "https://"+ad
        #print(ad)
    #b.clear()
    k = 1

#https://qastack.info.tr/programming/7160737/python-how-to-validate-a-url-in-python-malformed-or-not
    def reg(ad):
        regex = re.compile(
                r'^(?:http|ftp)s?://' # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                r'localhost|' #localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                r'(?::\d+)?' # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        return regex

#print(re.match(regex, ad) is not None) # True-False
    if(re.match(reg(ad), ad)is None):
            r1 = re.match(ad,"https://")
            r2 = re.match(ad,"http://")
            if(r1 is None and r2 is None):
                ad = "https://"+ad
    
    
    if(re.match(reg(ad),ad)is None):


                
        


            print('Address/netmask is invalid for IPv4:', ad)
            k=0



    def explanation(x):

        code = [100,101,102,200,201,202,203,204,205,206,207,210,300,301,302,303,304,305,307,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,422,423,424,500,501,502,503,504,505]
        message = ["Continue","Switching Protocols","Proccessing","OK","Created","Accepted", "Non-Authoritative Information","No Content", "Reset Content","Partial Content","Multi-Status","Content Different","Multiple Choises","Moved Permanently","Multiple Temporarily","See Other","Not Modified","Use Proxy","Temporary Redirect","Bad Request","Unauthorized","Payment Required","Forbidden","Not Found","Nonaccess","Not Acceptable","Needed Proxy","Time-out","Conflict","Gone","Length Required","Precondition Failed","Request Entity Too Large","Request-URI Too Long","Unsupported Media Type","Requested Range Unstatifiable","Expectation Failed","Unprocessable Entity","Loced","Method Failure","Internal Server Error","Unapplied","Bad Gateway","No Service","Gateway Timeout","HTTP Version not Supported"]
        for i in range(0,len(code)):

            if(x==code[i]):

                return (message[i])

        return(404)




    while(k==1):

        print("Please, choose one of requests in below and type the number:\n1-POST\n2-PUT\n3-DELETE\n4-HEAD\n5-PATCH\n6-OPTIONS\n7-GET\n8-Change Address\n0-Exit")
        x = int(input("Number:"))

        if(x == 1):

            key = input("A key for POST option: ")
            value = input("A value for POST option: ")

            try:
                adpost = requests.post(ad, data = {key:value})
                adpost.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')  
            except Exception as err:
                print(f'Other error occurred: {err}')  
            else:
                print(adpost)
                print(explanation(adpost.status_code))
    
        if(x == 2):


            key = input("A key for PUT option: ")
            value = input("A value for PUT option: ")
            try:
                adput = requests.put(ad, data = {key:value})
                adput.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}') 
            except Exception as err:
                print(f'Other error occurred: {err}')  
            else:
                print(adput)
                print(explanation(adput.status_code))

        if(x == 3):
            try:

                addel = requests.delete(ad)
                addel.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')  
            except Exception as err:
                print(f'Other error occurred: {err}') 
            else:
                print(addel)
                print(explanation(addel.status_code))
        if(x == 4):

            try:
                adhead = requests.head(ad)
                adhead.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')  
            else:
                print(adhead)
                print(explanation(adhead.status_code))

        if(x == 5):


            key = input("A key for PATCH option: ")
            value = input("A value for PATCH option: ")
            try:

                adpatch = requests.patch(ad, data ={key:value})
                adpatch.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')  
            except Exception as err:
                print(f'Other error occurred: {err}')  
            else:
                print(adpatch)
                print(explanation(adpatch.status_code))




        if(x == 6):
            try:

                adoptions = requests.options(ad)
                adoptions.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}') 
            except Exception as err:
                print(f'Other error occurred: {err}')  
            else:
                print(adoptions)
                print(explanation(adoptions.status_code))
    
        if(x == 7):
            try:
                adget = requests.get(ad)
                adget.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}') 
            except Exception as err:
                print(f'Other error occurred: {err}')  
            else:
                print(adget)
                print(explanation(adget.status_code))
        if(x==8):
            break

        if(x == 0):

            break

    if(x==0):
        break

