import sqlite3

def remove_item(item_id):
    # Connect to the database
    conn = sqlite3.connect('inventory.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Delete the item from the inventory table
    cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()
