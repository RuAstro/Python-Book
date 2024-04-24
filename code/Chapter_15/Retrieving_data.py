import sqlite3

values = (
    ("Ron", "Obvious", 42),
    ("Luigi", "Vercotti", 43),
    ("Arthur", "Belling"28),
)

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute("Drop table if exists People")
    cursor.execute("""
        Create table People(
            FirstName TEXT,
            LastName TEXT,
            Age INT
        );"""
    )
    
    cursor.executemany("Insert into people VALUES(?, ?, ?);", values)
    
    #Select all first and last names from people over age 30
    cursor.execute(
        "Select FirstName, LastName From people where age > 30;"
    )
    for row in cursor.fetchall():
        print(row)