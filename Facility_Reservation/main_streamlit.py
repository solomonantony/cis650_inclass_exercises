import streamlit as st
import db, services, config
import pandas as pd

# """ streamlit.cache_reource is a Python decorator in Streamlit used to cache global, unserializable 
# objects—such as machine learning models and database connections—so they 
# do not reload on every app rerun. Instead of creating a copy, it stores a 
# single shared instance in memory and reuses it across all users, sessions, 
# and interactions (https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)
#  """

@st.cache_resource            # runs once per server process, not on every rerun
def setup_database():
    db.init_db()
    return True
setup_database()
conn = db.get_connection()




setup_database()
conn = db.get_connection()    # the script reruns on every click, so connect each run

st.title("Room Reservations")
tab_customers, tab_book, tab_manage, tab_reports, tab_about = st.tabs(
    ["Customers", "New Reservation", "Manage", "Reports", "About"])

# ---------- Customers ----------
with tab_customers:
    with st.form("new_customer", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        customer_saved = st.form_submit_button("Save customer")
    if customer_saved:
        try:
            c = services.save_customer(conn, name, email, phone)
            st.success(f"Saved customer {c}")
        except ValueError as e:
            st.error(str(e))
    st.dataframe(services.list_customers(conn)) #display the list of customers


with tab_book:
    customers = services.list_customers(conn)
    customers_df = pd.DataFrame(customers)
    if not customers:
        st.info("Add a customer first.")
    else:
        with st.form("new_reservation", clear_on_submit=True):
            #customers = {f"{c['name']} (#{c['id']})": c["id"] for c in customers}
            selected_customer_name = st.selectbox("Customer", customers_df["name"])
            desired_day = st.date_input("Date")
            rooms = [c['Name'] for c in config.ROOMS]
            selected_room = st.selectbox("Room", rooms)
            attendees = int(st.number_input("Attendees", min_value=1, value=1, max_value=60))
            reservation_saved = st.form_submit_button("Save reservation")
        if reservation_saved:
            try:
                selected_customer_id = pd.DataFrame(services.find_customer(conn, selected_customer_name))[0]["id"]
                reservation = services.make_reservation(conn,selected_customer_id,selected_room, desired_day, attendees, "Requested")
                st.success(f"Saved reservation id #{reservation}")
            except ValueError as e:
                st.error(str(e))
    st.dataframe(services.list_reservations(conn))

with tab_manage:
    reservations = services.list_reservations(conn)
    reservations_df = st.dataframe(reservations, on_select="rerun",selection_mode="single-row", use_container_width=True)
    if reservations_df:
         selected_reservation = reservations_df.selection.rows
         if selected_reservation:
             row_index = selected_reservation[0]
             #st.write(row_index)
             default_id = reservations[row_index]["id"]
             #st.write(default_id)
             default_room = reservations[row_index]["room"]
             default_room_id = services.get_room_id(default_room)
             default_customer_id = reservations[row_index]["customer_id"]
             request_date = reservations[row_index]["request_date"]
             default_attendees=reservations[row_index]["attendees"]
             status=  reservations[row_index]["status"]
             with st.form("edit_reservation_form"):
                 st.subheader("Edit Reservation")
                 id = st.text_input("Id", value=default_id, disabled=True)
                 customer_id = st.text_input("Customer id", value=default_customer_id, disabled=True)
                 rooms = [c['Name'] for c in config.ROOMS]
                 new_room = st.selectbox("Room", rooms, index=default_room_id)
                 new_attendees = st.number_input("Attendees", value=default_attendees, min_value=1, max_value=60)
                 assigned_date = st.date_input("Date Assigned", value=request_date)
                 submitted = st.form_submit_button("Save changes")
                 if submitted:
                     services.change_reservation(conn, reservation_id=default_id, requested_room=new_room,assigned_date=assigned_date, new_attendees=new_attendees, new_status="Assigned")
                     st.success(f"Saved reservation")
                 



conn.close()
