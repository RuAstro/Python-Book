import sqlite3

# CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)
# INSERT INTO People VALUES('Ron', 'Obvious', 42)

create_table = """
CREATE TABLE People(
    FirstName Text,
    LastName Text,
    Age INT
);"""

insert_values = """
INSERT INTO People VALUES(
    'Ron',
    'Obvious'
    42
);"""

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
cursor.execute(create_table)
cursor.execute(insert_values)

connection.commit()
connection.close()


with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute(create_table)
    cursor.execute(insert_values)
