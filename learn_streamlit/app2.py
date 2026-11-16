import streamlit as st

st.title("Customers (practice)")

# read https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state 
if "customers" not in st.session_state:  # Initialize the session state variable
    st.session_state.customers = []

with st.form("new_customer", clear_on_submit=True): #creates a form, adds widgets, and a submit button
    name = st.text_input("Name")
    email = st.text_input("Email")
    saved = st.form_submit_button("Save customer")

if saved:  #when the submit button is pressed
    if not name.strip():
        st.error("Name is required")
    else:
        st.session_state.customers.append({
            "id": len(st.session_state.customers) + 1,
            "name": name.strip(),
            "email": email.strip(),
        })
        st.success("Saved")

if st.session_state.customers: #keep updating the dataframe when new customers are added
    st.dataframe(st.session_state.customers, hide_index=True)
else:
    st.info("No customers yet.")
