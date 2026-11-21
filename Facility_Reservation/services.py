import config
import repository
def valid_customer(conn, customer_id):
    sql_statement = "Select * from customers where id = ?"
    args = (customer_id,)
    cursor = conn.cursor()
    cursor.execute(sql_statement, args)
    return cursor.fetchone()

def save_customer(conn, name, email, phone):
    customer_id = repository.add_customer(conn=conn, name=name, email=email, phone=phone)
    return customer_id

def valid_room(requested_room):
    for room in config.ROOMS:
        if room["Name"] == requested_room:
            return room
    return None


def make_reservation(conn, customer_id, requested_room, request_date, attendees, status): # return a room if valid reservation request
    if not valid_customer(conn, customer_id):
        raise ValueError("Invalid customer_id")
    room = valid_room(requested_room)
    if room is None:
        raise ValueError("Unknown room")
    if attendees < 1:
        raise ValueError("Attendees must be atleast 1")
    if attendees > room["capacity"]:
        raise ValueError("Room capacity is too small")
    if not repository.check_availability(conn, room["Name"], request_date):
        raise ValueError("Room not available for the requested date")
    if status not in ["Requested", "Assigned", "Cancelled", "Completed"]:
        raise ValueError("Invalid reservation status")
    reservation_id = repository.add_reservation(conn, customer_id, requested_room, request_date, attendees, status)
    return reservation_id
    
def cancel_reservation(conn, reservation_id):
    reservation = repository.get_reservation(conn, reservation_id=reservation_id)
    if reservation is None:
        raise LookupError("Reservation not found")
    if reservation["status"] == "cancelled":
        raise ValueError ("Reservation is already cancelled")
    repository.set_reservation_status(conn, reservation_id, "cancelled")
    return repository.get_reservation(conn, reservation_id)

def change_reservation(conn, reservation_id, requested_room, assigned_date, new_attendees, new_status):
    reservation = repository.get_reservation(conn, reservation_id=reservation_id)
    if reservation is None:
        raise LookupError("Reservation not found")
    if reservation["status"] == "Cancelled":
        raise ValueError ("Cancelled reservation cannot be changed")
    if not repository.check_availability(conn, requested_room, assigned_date):
        raise ValueError("Room not available for the requested date")
    room = valid_room(requested_room)
    if new_attendees > room["capacity"]:
        raise ValueError("Room capacity is too small")
    if repository.update_reservation(conn, reservation_id=reservation_id, room=requested_room, attendees=new_attendees, assigned_date=assigned_date, status=new_status):
        return True
    else:
        raise ValueError("Error updating reservation")
    

def list_customers(conn):
    return repository.get_customers(conn)

def list_reservations(conn):
    return repository.get_reservations(conn)

def find_customer(conn, name):
    return repository.get_customer_by_name(conn, name)

def get_room_id(room_name):
    for index, room in enumerate(config.ROOMS):
        if room["Name"] == room_name:
            return index

    