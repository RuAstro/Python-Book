# Avoid Security Issues With Parametrized Statements

import sqlite3

# get person data from user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
data = (first_name, last_name, age)

# Execute insert statement for supplied person data
query = "INSERT INTO People Values" f"(('{first_name}', '{last_name}', '{age}'));"
with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute(query)

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO People VALUES(?, ?, ?);", data)

cursor.execute(
    "Update People SET Age=? WHERE FirstName? AND LastName=?;"(45, "Luigi", "Vercotti")
)
