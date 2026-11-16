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

def get_customer(conn, customer_id):
    row = conn.execute("SELECT * from customers where id = ?", (customer_id,)).fetchone()
    return dict(row) if row else None

def list_customers(conn):
    rows = conn.execute("SELECT * from customers ORDER BY name").fetchall()
    return [dict(r) for r in rows] # return a list of dictionaries

def update_reservation(conn, reservation_id, room, assigned_date, attendees):
    conn.execute(
        """UPDATE reservations set room = ?, assigned_date= ?, attendees = ? where id = ?""",
        (room, assigned_date, attendees, reservation_id))
    conn.commit()

def set_reservation_status(conn, reservation_id, status):
    conn.execute(
        """UPDATE reservations SET status = ? where id = ?""", 
        (status, reservation_id))
    conn.commit()

def get_reservation(conn, reservation_id):
    row = conn.execute("SELECT * from reservation where id =?", (reservation_id,)).fetchone()
    return dict(row) if row else None

def check_availability(conn, requested_room, request_date):
    row = conn.execute("SELECT * from reservations where assigned_date= ? and room = ?", (request_date, requested_room,)).fetchone()
    return dict(row) if row else None


