import sqlite3

def update_purchase_date(item_id, new_purchase_date):
    # Connect to the database
    conn = sqlite3.connect('inventory.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Update the purchase date of the item
    cursor.execute("UPDATE inventory SET purchase_date = ? WHERE id = ?", (new_purchase_date, item_id))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()
