import mechanicalsoup

# You create a Browser instance and use it to request the http://olympus.realpython.org/login page.
# You assign the HTML content of the page to the login_html variable using the .soup property.
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = browser.get(url)
login_html = login_page.soup()

# login_html.select("form") returns a list of all <form> elements on the page.
form = login_html.select("form")[0]
form.select("input")[0]["values"] = "zeus"
form.select("input")[1]["values"] = "ThunderDude"

profile_page = browser.submit(form, login_page.url)

links = profile_page.soup.select("a")

for link in links:
    address = link["href"]
    text = link.text

print(f"{text}: {address}")
