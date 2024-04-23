from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)

page

html_bytes = page.read()
html = html_bytes("utf-8")

print(html)

# >>> html = html_bytes.decode("utf-8")
# >>> print(html)
# <html>
# <head>
# <title>Profile: Aphrodite</title>
# </head>
# <body bgcolor="yellow">
# <center>
# <br><br>
# <img src="/static/aphrodite.gif" />
# <h2>Name: Aphrodite</h2>
# <br><br>
# Favorite animal: Dove
# <br><br>
# Favorite color: Red
# <br><br>
# Hometown: Mount Olympus
# </center>
# </body>
# </html>

title_index = html.find("<title>")
title_index

start_index = title_index + len("<title>")
start_index

end_index = html.find("</title>")
end_index

title = html[start_index:end_index]
title

page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
title
#'\n<head>\n<title >Profile: Poseidon'
