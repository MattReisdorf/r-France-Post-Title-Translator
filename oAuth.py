#MReisdorf_Bot OAuth

import requests
import requests.auth




"""

client_auth = requests.auth.HTTPBasicAuth('CLIENT_ID' , 'CLIENT_SECRET')
post_data = {"grant_type": "password" , "username": "USERNAME" , "password": "PASSWORD"}
headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
response = requests.post("https://www.reddit.com/api/v1/access_token" , auth=client_auth, data=post_data, headers=headers)
print(response.json())
print("\n")



"""

headers = {"Authorization": "bearer 576119863287-cO85P1mEL6-nuKyu83yhWOghlauUAw" , "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
response = requests.get("https://oauth.reddit.com/api/v1/me" , headers = headers)
print(response.json())
