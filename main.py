import sqlite3
from datetime import date, datetime, timedelta

# Database initiation should be moved out of main and into startDatabase.py.

# Connect to the database
conn = sqlite3.connect('inventory.db')

# Create a cursor object
cursor = conn.cursor()

# Create readiness table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS readiness (
    readiness_id INTEGER PRIMARY KEY AUTOINCREMENT,
    readiness TEXT NOT NULL
    )
""")

# Create foodtype table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS foodtype (
    foodtype_id INTEGER PRIMARY KEY AUTOINCREMENT,
    foodtype TEXT NOT NULL
    )
""")

# Create foodclass table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS foodclass (
    foodclass_id INTEGER PRIMARY KEY AUTOINCREMENT,
    foodclass TEXT NOT NULL
    )
""")

# Create units table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS units (
    unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    unitname TEXT NOT NULL,
    unitclass TEXT NOT NULL
    )
""")

# Create ingredients table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    variety TEXT NOT NULL,
    class,
    type,
    foodtype TEXT NOT NULL
    )
""")

# Create the inventory table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_id,
    type_id,
    class_id,
    quantity TEXT NOT NULL,
    uint_id,
    purchase DATE NOT NULL,
    expiration DATE NOT NULL
    )
""")

# Create the estimated_expirations table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS estimated_expirations (
    food_id INTEGER PRIMARY KEY AUTOINCREMENT,
    days_to_expire INTEGER NOT NULL
    )
""")


# Commit the changes
conn.commit()

# Sample data needs reformating since last update
# Sample data with estimated expiration dates
cursor.execute("INSERT INTO inventory VALUES"
               "(NULL, 'Apple', 'Fresh', 'Fruit', '3', '2023-04-20')"
)
cursor.execute("INSERT INTO inventory VALUES"
               "(NULL, 'Banana', 'Fresh', 'Fruit', '5', '2023-04-20')"
)
cursor.execute("INSERT INTO inventory VALUES"
               "(NULL, 'Milk', 'Fresh', 'Dairy', '1', '2023-04-20')"
)
cursor.execute("INSERT INTO inventory VALUES"
               "(NULL, 'Milk', 'Pasteurized', 'Dairy', '1', '2023-04-20')"
)
cursor.execute("INSERT INTO inventory VALUES"
               "(NULL, 'Milk', 'UTH', 'Dairy', '1', '2023-04-20')"
)
cursor.execute("INSERT INTO inventory VALUES"
               "(NULL, 'Bread', 'Fresh', 'Grain', '3', '2023-04-20')"
)

# Sample estimated expiration times
cursor.execute("INSERT INTO estimated_expirations VALUES"
               "(NULL, 'Apple', 'Fresh', 'Fruit', '15')"
)
cursor.execute("INSERT INTO estimated_expirations VALUES"
               "(NULL, 'Banana', 'Fresh', 'Fruit', '10')"
)
cursor.execute("INSERT INTO estimated_expirations VALUES"
               "(NULL, 'Milk', 'Fresh', 'Dairy', '3')"
)
cursor.execute("INSERT INTO estimated_expirations VALUES"
               "(NULL, 'Milk', 'Pasteurized', 'Dairy', '7')"
)
cursor.execute("INSERT INTO estimated_expirations VALUES"
               "(NULL, 'Milk', 'UTH', 'Dairy', '90')"
)
cursor.execute("INSERT INTO estimated_expirations VALUES"
               "(NULL, 'Bread', 'Fresh', 'Grain', '4')"
)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
