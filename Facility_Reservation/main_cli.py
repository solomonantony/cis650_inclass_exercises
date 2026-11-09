import  db
import repository
def add_customer_ui():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    conn = db.get_connection()
    customer_id = repository.add_customer(conn, name, email, phone)
    return customer_id

def display_menu():
    while True:
        print("""
            1: Create database
            2: Create a customer
            3: Create a Reservation
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




if __name__ == "__main__":
    display_menu()
