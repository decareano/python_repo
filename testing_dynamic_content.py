import re
import urllib.request
response = urllib.request.urlopen('http://www.afa.com.ar/deposito/html/v3/index.html?channel=deportes.futbol.primeraa.448792&lang=es_LA')
html = response.read()
text = html.decode()
re.findall('(.*?)',text)