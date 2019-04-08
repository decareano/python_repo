import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://www.racefans.net/2019/03/31/2019-bahrain-grand-prix-interactive-data-lap-charts-times-and-tyres/')
# http = urllib3.PoolManager()
# r = http.request('GET', 'http://www.racefans.net/2019/03/31/2019-bahrain-grand-prix-interactive-data-lap-charts-times-and-tyres/')
soup = BeautifulSoup(r.data, 'html.parser')
print (soup.title)
print (soup.title.text)
