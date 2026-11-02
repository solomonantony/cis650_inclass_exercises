# this script creates an database for the Facility Reservation application
import sqlite3
import pandas as pd
def create_table(sql_statement, connection):
    cursor = connection.cursor()
    cursor.execute(sql_statement)
   

connection = sqlite3.connect("./facility_reservation/facility_reservation.db")
cursor = connection.cursor()
create_customer_sql = """CREATE TABLE if not exists Customer 
                        (customer_id int primary key,
                        customer_name text,
                        contact_name text,
                        business_address text,
                        contact_phone text)"""



#cursor.execute("select name from sqlite_master where type ='table'")

tables_df = pd.read_sql("select name from sqlite_master where type ='table'", connection)
print(tables_df)

customers_df = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'customer_name': ['ABC Inc', 'DEF Inc', 'XYZ Inc'],
    'contact_name': ['Andy', 'Woody', 'Becky'],
    'business_address': ['123 Main Street', '345 Main Street', '890 Main Street'],
    'contact_phone': ['555-1234', '555-2345', '555-4567']
})
customers_df.to_sql('customer', con=connection, 
                    if_exists='append', index = False, 
                    index_label='customer_id')
print(pd.read_sql("Select * from customer", con=connection))

