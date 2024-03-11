import requests

res=requests.get('https://github.com/shreya-madhwal')
print(res.text)
print(res.elapsed)
print(res.headers['content-type'])
print(res)