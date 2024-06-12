# Adding an item to the database
def add_item(item_name, item_type, item_quantity=1, purchase_date=None,
                item_class="Fresh", expiration_date=None):

                new_item = True

                # Calculate todays date if purchase date not provided
                if purchase_date is None:
                today = date.today()
                purchase_date = today.isoformat()

                # Calculate the expiration date if not provided
                if expiration_date is None:
                cursor.execute(
                                "SELECT days_to_expire FROM estimated_expirations WHERE"
                                "name = ? and type = ? and class = ?",
                                (item_name, item_type, item_class,)
                )
                row = cursor.fetchone()
                estimated_days_to_expire = row[0] if row else 999
                expiration_date = (datetime.fromisoformat(purchase_date) + 
                                timedelta(days=estimated_days_to_expire))

                # Check if the item is alreay in the database. If it is add the quantity to the 
                # existing item, change the purchase date to the latest date,
                # and the expiration date to the earliest expiration. Otherwise, add a new item.
                cursor.execute("SELECT id, purchase, expiration FROM inventory WHERE"
                                "name = ? and type = ? and class = ?",
                                (item_name, item_type, item_class,)
                )
                row = cursor.fetchone()
                if row:
                # Item already exists, update the quantity.
                cursor.execute("UPDATE inventory SET quantity = ? WHERE id = ?",
                                (item_quantity + row[0], row[0],)
                )
                # Update the purchase date to the latest date.
                cursor.execute("UPDATE inventory SET purchase = ?"
                                "if current = ? > latest = ? WHERE id = ?",
                                (purchase_date, purchase_date, row[1], row[0],)
                )
                # Update the expiration date to the earliest expiration.
                cursor.execute("UPDATE inventory SET expiration = ?"
                                "if current = ? < earliest = ? WHERE id = ?",
                                (expiration_date, expiration_date, row[2], row[0],)
                )

                new_item = False

                # Insert the new item into the inventory table
                if new_item:
                cursor.execute("INSERT INTO inventory VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                                (item_name, item_class, item_type,
                                item_quantity, purchase_date, 
                                expiration_date.isoformat())
                )

                # Commit the changes
                conn.commit()
