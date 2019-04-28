from urllib.request import urlopen as uReq  #grabs the page
from bs4 import BeautifulSoup as soup       #parses html text

my_url = 'https://kith.com/collections/mens-footwear'



uClient = uReq(my_url)      #opening up connection, grabbing the page and downloads
page_html = uClient.read()      # stores page html into a variable
uClient.close()         #closes when done with it


page_soup = soup(page_html, "html.parser")  #html parses

containers = page_soup.findAll("div",{"class":"product-card"}) #grabs each product, on kith site in div thats names product-card


for container in containers:
    size = container.ul.li.button  #looks at specific html tags
    sizes = container.findAll("button")


print("Available sizes are: ")
for i in range(len(sizes)):
    size_range=[sizes[i].text]
    print(sizes[i].text)
