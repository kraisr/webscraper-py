import requests
from bs4 import BeautifulSoup

url = input("Paste your desired URL: ")
if (url[:7] != "htts://"):
    temp = "https://"
    url = temp + url

page = requests.get(url)
content = BeautifulSoup(page.content, "html.parser")

print(content.prettify)