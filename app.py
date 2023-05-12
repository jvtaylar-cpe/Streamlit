import streamlit as st

# Get the first number from the user.
first_number = st.number_input("Enter the first number:")

# Get the second number from the user.
second_number = st.number_input("Enter the second number:")

# Multiply the two numbers and print the result.
product = first_number * second_number
st.write("The product of the two numbers is", product)
