def add_customer(conn, name, email, phone):
    cursor= conn.execute(
        "INSERT INTO customers (name, email, phone) VALUES(?, ?, ?)",
        (name, email, phone)
    )
    conn.commit()
    return cursor.lastrowid

def add_reservation(conn, customer_id, room, request_date, attendees, status):
    cursor = conn.execute(
        "INSERT INTO reservations(customer_id, room, request_date, attendees, status) VALUES(?,?,?,?,?)",
        (customer_id, room, request_date, attendees, status)
    )
    conn.commit()
    return cursor.lastrowid

def get_customer(conn, customer_id):
    row = conn.execute("SELECT * from customers where id = ?", (customer_id,)).fetchone()
    return dict(row) if row else None

def get_customer_by_name(conn, name):
    row = conn.execute("SELECT * from customers where name = ?", (name,)).fetchone()
    return dict(row) if row else None
    

def get_customers(conn):
    cursor = conn.execute("SELECT * from customers ORDER BY name")
    columns = [col[0] for col in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()] # return a list of dictionaries
    return results

def get_reservations(conn):
    cursor = conn.execute("Select * from reservations order by id desc")
    columns = [col[0] for col in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()] # return a list of dictionaries
    return results

def update_reservation(conn, reservation_id, room, assigned_date, attendees, status):
    conn.execute(
        """UPDATE reservations set room = ?, assigned_date= ?, attendees = ?, status = ? where id = ?""",
        (room, assigned_date, attendees, status, reservation_id))
    conn.commit()
    return True

def set_reservation_status(conn, reservation_id, status):
    conn.execute(
        """UPDATE reservations SET status = ? where id = ?""", 
        (status, reservation_id))
    conn.commit()

def get_reservation(conn, reservation_id):
    cursor = conn.execute("SELECT * from reservations where id =?", (reservation_id,))
    row = cursor.fetchone()
    if row is None:
        return None
    columns = (col[0] for col in cursor.description)
    return dict(zip(columns, row))


def check_availability(conn, requested_room, request_date):
    row = conn.execute("SELECT * from reservations where assigned_date= ? and room = ?", (request_date, requested_room,)).fetchone()
    return False if row else True


