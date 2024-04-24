import sqlite3
from pathlib import Path
import os

database = "roster.db"
os.remove(database)

# Creating db and table.
create_table = """
CREATE TABLE People(
    FirstName Text,
    SpeciesName Text,
    Age INT
);"""
# Add data
insert_values1 = """
INSERT INTO People VALUES(
    'Benjamin',
    'Sisko',
    40
);"""

insert_values2 = """
INSERT INTO People VALUES(
    'Jadzia-Dax',
    'Trill',
    300
);"""

insert_values3 = """
INSERT INTO People VALUES(
    'Kira-Nerys',
    'bajordan',
    29
);"""

with sqlite3.connect(database) as connection:
    cursor = connection.cursor()
    cursor.execute(create_table)
    cursor.execute(insert_values1)
    cursor.execute(insert_values2)
    cursor.execute(insert_values3)

# Update method
# cursor.execute("UPDATE data SET Name=?", ("Ezri dax", "Jadiza Dax"))

# cursor.execute("Select Name, Where Species='Barjoran', Age ")
# for row in cursor.fetchall():
#     print(row)
