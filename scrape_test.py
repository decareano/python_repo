from bs4 import BeautifulSoup
import requests
page_link ='https://www.southwest.com'
# fetch the content from url
page_response = requests.get(page_link, timeout=5)
# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")

# extract all html elements where price is stored
prices = page_content.find(id='air-booking-fares-0-1')
# prices has a form:
#[<div class="main_price">Price: $66.68</div>,
# <div class="main_price">Price: $56.68</div>]

# you can also access the main_price class by specifying the tag of the class
# prices = page_content.find_all('div', attrs={'class':'fare-button'})

print(page_content.prettify())
  
