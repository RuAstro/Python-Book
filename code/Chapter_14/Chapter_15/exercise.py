import sqlite3

# Creating db and table.
connection = sqlite3.connect("roster.db")
cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS ROSTER (
               Name TEXT,
               Species TEXT,
               Age,
               )"""
)

connection.commit()
connection.close()

# Adding data
data = (
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajordan", 29),
)

cursor.executemany("Insert Into Roster VALUES(?, ?, ?)", data)

# Update method
cursor.execute("UPDATE data SET Name=?", ("Ezri dax", "Jadiza Dax"))

cursor.execute("Select Name, Where Species='Barjoran', Age ")
for row in cursor.fetchall():
    print(row)
