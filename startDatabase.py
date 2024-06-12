import sqlite3
# Connect to the database
conn = sqlite3.connect('inventory.db')
# Create a cursor object
cursor = conn.cursor()
# Create the inventory table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    item_type TEXT NOT NULL,
    purchase_date DATE NOT NULL,
    expiration_date DATE NOT NULL
)
''')
# Sample data
cursor.execute("INSERT INTO inventory VALUES (NULL, 'Apple', 'Fruit', '2023-04-20', '2023-04-27')")
cursor.execute("INSERT INTO inventory VALUES (NULL, 'Banana', 'Fruit', '2023-04-20', '2023-04-27')")
cursor.execute("INSERT INTO inventory VALUES (NULL, 'Milk', 'Dairy', '2023-04-20', '2023-04-27')")
cursor.execute("INSERT INTO inventory VALUES (NULL, 'Bread', 'Grain', '2023-04-20', '2023-04-27')")
# Commit the changes
conn.commit()
# Close the connection
conn.close()
