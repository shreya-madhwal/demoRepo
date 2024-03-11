# import requests module 
import requests 
from requests.auth import HTTPBasicAuth 
# Making a get request 
response = requests.get('https://api.github.com /shreya-madhwal', 
            auth = HTTPBasicAuth('shreya-madhwal', 'Risss123@')) 
# print request object 
print(response) 