from urllib import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
page

for tag in ["Name: ", "Fav Color: "]:
    tag_start = html_text.find(tag) + len(tag)
    tag_end = html_text[tag_start:].find("<")
    print(tag)
