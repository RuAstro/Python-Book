import sqlite3

connection = sqlite3.connect("test_database.db")

cursor = connection.cursor()
type(cursor)

query = "SELECT datetime('now', 'localtime');"
results = cursor.execute(query)
results

row = results.fetchone()
row
("2018-11-20 23:07:21",)

time = row[0]
time

connection.close()
