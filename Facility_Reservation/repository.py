def add_customer(conn, name, email, phone):
    cursor= conn.execute(
        "INSERT INTO customers (name, email, phone) VALUES(?, ?, ?)",
        (name, email, phone)
    )
    conn.commit()
    return cursor.lastrowid

def make_reservation(conn, customer_id, room, request_date, attendees, status):
    cursor = conn.execute(
        "INSERT INTO reservations(customer_id, room, request_date, attendees, status) VALUES(?,?,?,?,?)",
        (customer_id, room, request_date, attendees, status)
    )
    conn.commit()


    return cursor.lastrowid

def get_customer():
    pass

