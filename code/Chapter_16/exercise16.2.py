from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

url = "http://olympus.realpython.org/profiles"
# page = urlopen(url)
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:  # to check if "href" attribute exists
        links.append(href)

for link in links:
    # Get the URL of the page
    full_url = urlopen(url, link)
    # Send a GET request to the page URL
    page_response = requests.get(full_url)
    # Parse the HTML content of the page
    page_soup = BeautifulSoup(page_response.text, "html.parser")
    # Get the text of the page without HTML tags
    page_text = page_soup.get_text()

    print(page_text)
