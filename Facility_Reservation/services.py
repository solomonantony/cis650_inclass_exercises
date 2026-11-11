import config
import repository
def valid_customer(conn, customer_id):
    sql_statement = "Select * from customers where id = ?"
    args = (customer_id,)
    cursor = conn.cursor()
    cursor.execute(sql_statement, args)
    return cursor.fetchone()

def valid_room(requested_room):
    for room in config.ROOMS:
        if room["Name"] == requested_room:
            return room
    return None
def request_reservation(conn, customer_id,requested_room,request_date,attendees, status):
    if not valid_customer(conn, customer_id):
        raise ValueError("Invalid customer_id")
    room = valid_room(requested_room)
    if room is None:
        raise ValueError("Unknown room")
    if attendees < 1:
        raise ValueError("Attendees must be atleast 1")
    if attendees > room["capacity"]:
        raise ValueError("Room capacity is too small")
    if status not in ["Requested", "Assigned", "Cancelled", "Completed"]:
        raise ValueError("Invalid reservation status")
    reservation_id = repository.make_reservation(conn, customer_id, requested_room, request_date, attendees, status)
    return reservation_id
    




    