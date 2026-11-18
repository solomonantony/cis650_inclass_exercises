import streamlit as st
import db, services, config


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
tab_customers, tab_book, tab_manage, tab_reports = st.tabs(
    ["Customers", "New Reservation", "Manage", "Reports"])

# ---------- Customers ----------
with tab_customers:
    with st.form("new_customer", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        saved = st.form_submit_button("Save customer")
    if saved:
        try:
            c = services.register_customer(conn, name, email, phone)
            st.success(f"Saved customer {c['id']}")
        except ValueError as e:
            st.error(str(e))
    st.dataframe(services.list_customers(conn)) #display the list of customers
# Other tabs to added


with tab_book:
    customers = services.list_customers(conn)
    if not customers:
        st.info("Add a customer first.")
    else:
        customers = {f"{c['name']} (#{c['id']})": c["id"] for c in customers}
        selected_customer = st.selectbox("Customer", list(customers))
        desired_day = st.date_input("Date")
        rooms = {f"{c['Name']} ({c['capacity']})": c["capacity"] for c in config.ROOMS}
        selected_room = st.selectbox("Room", list(rooms))

        attendees = int(st.number_input("Attendees", min_value=1, value=1, max_value=60))


conn.close()
