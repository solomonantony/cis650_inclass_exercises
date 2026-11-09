def add_customer(conn, name, email, phone):
    cursor= conn.execute(
        "INSERT INTO customers (name, email, phone) VALUES(?, ?, ?)",
        (name, email, phone)
    )
    conn.commit()
    return cursor.lastrowid

def get_customer():
    pass

