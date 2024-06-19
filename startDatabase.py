import sqlite3
from datetime import date, datetime, timedelta

# Database initiation should be moved out of main.

# Connect to the database
conn = sqlite3.connect('inventory.db')

# Enable foreign key constraints
conn.execute('PRAGMA foreign_keys = ON')

# Create a cursor object
cursor = conn.cursor()

# Create readiness table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS readiness (
    readinessID INTEGER PRIMARY KEY AUTOINCREMENT,
    readiness TEXT NOT NULL
    )
""")

# Create foodtype table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS foodtype (
    foodtypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    foodtype TEXT NOT NULL
    )
""")

# Create foodclass table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS foodclass (
    foodclassID INTEGER PRIMARY KEY AUTOINCREMENT,
    foodclass TEXT NOT NULL
    )
""")

# Create units table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS units (
    unitID INTEGER PRIMARY KEY AUTOINCREMENT,
    unitname TEXT NOT NULL,
    unitclass TEXT NOT NULL
    )
""")

# Create ingredients table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
    ingredientID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    variety TEXT NOT NULL,
    classID INTEGER,
    typeID INTEGER,
    readinessID INTEGER,
    FOREIGN KEY (classID) REFERENCES foodclass(foodclassID),
    FOREIGN KEY (typeID) REFERENCES foodtype(foodtypeID),
    FORIEGN KEY (readinessID) REFERENCES readiness(readinessID)
    )
""")

# Create the inventory table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    inventoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredientID INTEGER,
    quantity INTEGER,
    unitID INTEGER,
    purchase DATE NOT NULL,
    expiration DATE NOT NULL,
    FOREIGN KEY (ingredientID) REFERENCES ingredients(ingredientID),
    FOREIGN KEY (unitID) REFERENCES units(unitID)
    )
""")

# Create the estimated_expirations table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS estimated_expirations (
    ingredientID INTEGER,
    days_to_expire INTEGER NOT NULL
    FORIEGN KEY (ingredientID) REFERENCES ingredients(ingredientID)
    )
""")


# Commit the changes
conn.commit()

# Sample readiness data
cursor.execute("INSERT INTO readiness VALUES"
               "(NULL, 'Raw')"
)
cursor.execute("INSERT INTO readiness VALUES"
               "(NULL, 'Half-Baked')"
)
cursor.execute("INSERT INTO readiness VALUES"
               "(NULL, 'Pre-Cooked')"
)
cursor.execute("INSERT INTO readiness VALUES"
               "(NULL, 'Cooked')"
)
cursor.execute("INSERT INTO readiness VALUES"
               "(NULL, 'Green')"
)
cursor.execute("INSERT INTO readiness VALUES"
               "(NULL, 'Under Ripe')"
)
cursor.execute("INSERT INTO readiness VALUES"
               "(NULL, 'Ripe')"
)
cursor.execute("INSERT INTO readiness VALUES"
               "(NULL, 'Over Ripe')"
)
cursor.execute("INSERT INTO readiness VALUES"
               "(NULL, 'Ready to Eat')"
)


# Sample foodtype data
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Vegetable')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Grain')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Legume')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Nut')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Fruit')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Pork')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Beef')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Fish')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Seafood')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Egg')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Dairy')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Poultry')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Oil')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Sauce')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Spice')"
)
cursor.execute("INSERT INTO foodtype VALUES"
               "(NULL, 'Mixed Ingredients')"
)

# Sample foodclass data
cursor.execute("INSERT INTO foodclass VALUES"
               "(NULL, 'Fresh')"
)
cursor.execute("INSERT INTO foodclass VALUES"
               "(NULL, 'Dried')"
)
cursor.execute("INSERT INTO foodclass VALUES"
               "(NULL, 'Pasteurized')"
)
cursor.execute("INSERT INTO foodclass VALUES"
               "(NULL, 'UHT')"
)
cursor.execute("INSERT INTO foodclass VALUES"
               "(NULL, 'Frozen')"
)
cursor.execute("INSERT INTO foodclass VALUES"
               "(NULL, 'Canned')"
)

# Sample units data
cursor.execute("INSERT INTO units VALUES"
               "(NULL, 'Gram', 'Weight')"
)
cursor.execute("INSERT INTO units VALUES"
               "(NULL, 'Pound', 'Weight')"
)
cursor.execute("INSERT INTO units VALUES"
               "(NULL, 'Ounce', 'Weight')"
)
cursor.execute("INSERT INTO units VALUES"
               "(NULL, 'Mililitre', 'Volume')"
)
cursor.execute("INSERT INTO units VALUES"
               "(NULL, 'Liquid Ounce', 'Volume')"
)
cursor.execute("INSERT INTO units VALUES"
               "(NULL, 'Cup', 'Volume')"
)
cursor.execute("INSERT INTO units VALUES"
               "(NULL, 'Gallon', 'Volume')"
)

# Sample ingredients data
cursor.execute("INSERT INTO ingredients VALUES"
               "(NULL, 'Beef', 'Minced', 1, 7, 1)"
)
cursor.execute("INSERT INTO ingredients VALUES"
               "(NULL, 'Pork', 'Chops', 5, 6, 1)"
)
cursor.execute("INSERT INTO ingredients VALUES"
               "(NULL, 'Chicken', 'Nuggets', 5, 12, 3)"
)
cursor.execute("INSERT INTO ingredients VALUES"
               "(NULL, 'Apple', 'Golden Granny', 1, 5, 5)"
)
cursor.execute("INSERT INTO ingredients VALUES"
               "(NULL, 'Peaches', 'In Syrup', 6, 5, 9)"
)
cursor.execute("INSERT INTO ingredients VALUES"
               "(NULL, 'Milk', 'Whole', 4, 11, 9)"
)
cursor.execute("INSERT INTO ingredients VALUES"
               "(NULL, 'Cheese', 'Camembert', 3, 11, 9)"
)
cursor.execute("INSERT INTO ingredients VALUES"
               "(NULL, 'Lasaña', 'Spinach', 1, 16, 4)"
)

# Sample inventory data with expiry dates
cursor.execute("INSERT INTO inventory VALUES"
               "(NULL, 1, 250, 1, '2024-04-20', '2024-04-30')"
)
cursor.execute("INSERT INTO inventory VALUES"
               "(NULL, 2, 1000, 1, '2024-04-20', '2024-08-30')"
)
cursor.execute("INSERT INTO inventory VALUES"
               "(NULL, 3, 500, 1, '2024-04-20', '2024-11-30'')"
)
cursor.execute("INSERT INTO inventory VALUES"
               "(NULL, 4, 200, 1, '2024-04-20', '2024-05-05')"
)
cursor.execute("INSERT INTO inventory VALUES"
               "(NULL, 5, 300, 1, '2024-04-20', '2025-05-01')"
)
cursor.execute("INSERT INTO inventory VALUES"
               "(NULL, 6, 1500, 4, '2024-04-20', '2024-09-13')"
)

# Add sample inventory data without expiration dates for estimation
# Add sample estimated expiration times

# Commit the changes
conn.commit()

# Close the connection
conn.close()
