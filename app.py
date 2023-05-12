import streamlit as st
import sqlite3

# Create a connection to the database.
conn = sqlite3.connect("contacts.db")
cur = conn.cursor()

# Create a header for the app.
st.header("CRUD Database App")

# Create UI elements.



# Display the value of the text input.
# st.write("Your name is", name)
text_input = st.text_input("Enter your name", key="name")
name = text_input.value

text_input = st.text_input("Enter your name", key="email")
email = text_input.value

text_input = st.text_input("Enter your name", key="phone")
phone = text_input.value


add_button = st.button("Add")
update_button = st.button("Update")
delete_button = st.button("Delete")

# Create a listbox to display the contacts.
listbox = st.selectbox("Select a contact:", [])

# Create a function to load the data from the database.
def load_data():
    # Delete all the items from the listbox.
    listbox.clear()

    # Get all the contacts from the database.
    cur.execute("SELECT * FROM contacts")
    contacts = cur.fetchall()

    # Add all the contacts to the listbox.
    for contact in contacts:
        listbox.append(contact[1])

# Load the data from the database when the app starts.
load_data()

# When the add button is clicked, add the contact to the database.
if add_button:
    name = name_entry.value
    email = email_entry.value
    phone = phone_entry.value

    cur.execute("INSERT INTO contacts(name,email,phone) VALUES(?,?,?)", (name,email,phone))
    conn.commit()

    load_data()

# When the update button is clicked, update the contact in the database.
if update_button:
    index = listbox.index(listbox.value)
    name = name_entry.value
    email = email_entry.value
    phone = phone_entry.value

    cur.execute("UPDATE contacts SET name=?, email=?, phone=? WHERE name=?",(name, new_email, new_phone, name))
    conn.commit()

    load_data()

# When the delete button is clicked, delete the contact from the database.
if delete_button:
    index = listbox.index(listbox.value)
    name = listbox.value

    cur.execute("DELETE FROM contacts WHERE name=?", (name,))
    conn.commit()

    load_data()

# Close the connection to the database when the app ends.
if __name__ == "__main__":
    conn.close()
