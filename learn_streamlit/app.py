import streamlit as st
st.title("Streamlit Practice")
st.caption("Step 4: Displaying text")
st.write("Hello")
st.caption("Step 5: Getting text input")

name = st.text_input("Your name")
st.write("Hello, ", name or "stranger", "!")

st.caption("Step 6: Displaying a button")
if st.button("Say hello"):
    st.write("Hello, ", name or "stranger", "!")

st.caption("Step 7: Dropdown list")
room = st.selectbox("Room", ["A101", "A102", "B201"])
st.write("You picked ", room) 

st.caption("Step 8: Number input")
people = st.number_input("Attendees", min_value=1, value=1, step=1, max_value=100) 
st.write("Attendees:", people)

st.caption("Step 9: Date picker")
day = st.date_input("Date")
st.write("You picked:", day, type(day))
st.write("As text:", str(day))

st.caption("Step 10: Time picker")
start = st.time_input("Start", step=900)
st.write("Start:", start.strftime("%H:%M"))
st.write("Database format:", f"{day} {start.strftime('%H:%M')}")

st.caption("Step 11: Error and Success alerts")
CAPACITY = {"A101": 10, "A102": 25, "B201": 60}
if people > CAPACITY[room]:
    st.error(f"{room} holds only {CAPACITY[room]} people")
else:
    st.success(f"{room} can hold your group")

st.caption("Step 12: Dataframe")
rows = [
    {"id": 1, "name": "Ana Lopez", "room": "A101"},
    {"id": 2, "name": "Ben Ortiz", "room": "B201"},
    {"id": 3, "name": "Lynn Jones", "room": "A102"},
]
st.dataframe(rows,hide_index = True)

st.caption("Step 13: Radio buttons as a side bar menu")
st.sidebar.title("Menu")
page = st.sidebar.radio("Go to", ["Home", "About", "Help"])
if page == "Home": st.title("Home")
if page == "About": st.title("About")
if page == "Help": st.title("Help")

st.caption("Step 14: Wdigets inside a form")
st.subheader("Without a form")
live = st.text_input("Type here (live)")
st.write("Live:", live)

st.subheader("With a from")
with st.form("demo_form"):
    batched = st.text_input("Type heere (batched)")
    sent = st.form_submit_button("Submit")
if sent:
    st.write("Submitted:", batched)


