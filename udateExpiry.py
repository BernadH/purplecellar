import sqlite3

def update_expiration_date(item_id, new_expiration_date):
    # Connect to the database
    conn = sqlite3.connect('inventory.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Update the expiration date of the item
    cursor.execute("UPDATE inventory SET expiration_date = ? WHERE id = ?", (new_expiration_date, item_id))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()
