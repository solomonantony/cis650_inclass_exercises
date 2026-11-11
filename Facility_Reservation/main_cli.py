import  db
import repository
import config
import datetime as dt
import services
def add_customer_ui():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    conn = db.get_connection()
    customer_id = repository.add_customer(conn, name, email, phone)
    return customer_id
def request_reservation_ui():
    
    customer_id = int(input("Customer ID: "))
    room = input(f"Room {[room['Name'] for room in config.ROOMS]}: ")
    request_date = dt.datetime.strptime(input("Request date mm/dd/yyyy: "),"%m/%d/%Y")
    attendees = int(input("Attendees: "))
    status = 'Requested'
    conn = db.get_connection()
    reservation_id = services.request_reservation(conn, customer_id, room, request_date, attendees, status)
    return reservation_id

def display_menu():
    while True:
        print("""
            1: Create database
            2: Create a customer
            3: Request a Reservation
            0: Quit
        """)
        user_choice = input("Select your option: ")
        if user_choice == '0':
            print("Thanks for trying this app.")
            break
        elif user_choice == '1':
            db.init_db()
        elif user_choice == '2':
            print("Customer added with id: ", add_customer_ui())
        elif user_choice == '3':
            print("Reservation was added ", request_reservation_ui())

if __name__ == "__main__":
    display_menu()
