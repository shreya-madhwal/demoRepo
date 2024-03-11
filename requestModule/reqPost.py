import requests
val={"topic":"example","body":"here's the topic"}
res1=requests.get('https://jsonplaceholder.typicode.com/posts')
print(res1.text)
print(res1.json)
print(res1.status_code)
res=requests.post('https://jsonplaceholder.typicode.com/posts',json=val)
print(res.json())
print(res.headers)
