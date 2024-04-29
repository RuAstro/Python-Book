import mechanicalsoup
from bs4 import BeautifulSoup
from datetime import datetime

browser = mechanicalsoup.Browser()
for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")

# time_paragraph = ("p", string="You rolled a die at ")
if time_paragraph:
    time_text = time_paragraph.find_next_sibling("p").text.strip()
    # Extract the time from the text
    time_string = time_text.split(" at ")[-1]
    # Parse the time string
    time = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")

    # Print the result and the current time
    print("Die Roll Result:", result)
    print("Current Time of the Quote:", time)
else:
    print("Current time not found.")
