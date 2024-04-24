from bs4 import BeautifulSoup
from urllib.request import urlopen

# Opens the URL using urlopen() from the urllib.request module
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)

# Reads the HTML from the page as a string and assigns it to the html variable
html = page.read().decode("utf-8")
# Creates a BeautifulSoup object and assigns it to the soup variable
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())

soup.find_all("img")
