import re
from urllib import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

# .*? non-greedily matches all text after the opening <TITLE >,
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)

image1, image2 = soup.find_all("img")
image1["src"]
# /static/dionysus.jpg'
image2["src"]
# /static/grapes.png'

soup.title.string
# Profile: Dionysus

print(title)
