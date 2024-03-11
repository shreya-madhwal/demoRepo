import requests
val={"topic":"example","body":"here's the topic"}

res=requests.put('https://httpbin.org/put',json=val)
print(res.json())