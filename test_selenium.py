import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
r = http.request('GET', 'https://http://www.afa.com.ar/deposito/html/v3/index.html?channel=deportes.futbol.primeraa.448792&lang=es_LA')
soup = BeautifulSoup(r.data, 'div')
print (soup.title)
print (soup.title.text)