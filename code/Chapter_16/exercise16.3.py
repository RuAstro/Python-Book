import mechanicalsoup

# create browser object and log in page
browser = mechanicalsoup.Browser()
url = " http://olympus.realpython.org/login"
login_page = browser.get(url)
# select login_form
login_form = login_page.soup.select("form")[0]
# the correct username and pass.
login_form.find("input", {"name": "user"})["value"] = "zeus"
login_form.find("input", {"name": "passwd"})["value"] = "ThunderDude"

response = browser.submit(login_form, login_page.url)

print(response.text)

# get title of the current page to verify
title = browser.get_current_page().title.text
print("Title of the current page:", title)

# back to previous page
browser.back()

# select login form again
login_form = browser.get_current_page().select("form")[0]

# Fill in the form fields with incorrect username and password
login_form.find("input", {"name": "user"})["value"] = "incorrect_username"
login_form.find("input", {"name": "passwd"})["value"] = "incorrect_password"

# Submit the form with incorrect input
response = browser.submit(login_form, login_page.url)

# check if the login process fails
if "Wrong username or password!" in response.text:
    print("Incorrect username or password.")
else:
    print("Successful")

print(response.text)
