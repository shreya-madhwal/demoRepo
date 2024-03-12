import requests
from bs4  import BeautifulSoup
res=requests.get('https://www.javatpoint.com/computer-network-tutorial')
print(res.status_code)
#print(res.content)
soup=BeautifulSoup(res.content,'html.parser')
#print(soup.prettify())

s=soup.find('div',class_='onlycontent')
content=s.find_all('p')
#print(content)
'''for line in content:
    print(line.text)

for x in soup.find_all('a'):
    print(x.get('href'))'''

for tag in soup.find_all():
    print(tag.name)
