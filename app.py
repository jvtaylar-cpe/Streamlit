import streamlit as st
import numpy as np

# Create a header for the calculator.
st.header("Scientific Calculator")

# Create a function to perform a mathematical operation on two numbers.

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
        
        
def calculate(operation, number1, number2):
    if operation == "+"):
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        return number1 / number2
    elif operation == "^":
        return np.power(number1, number2)
    elif operation == "log":
        return np.log(number1)
    elif operation == "sin":
        return np.sin(number1)
    elif operation == "cos":
        return np.cos(number1)
    elif operation == "tan":
        return np.tan(number1)
    elif operation == "sqrt":
        return np.sqrt(number1)
    else:
        raise ValueError("Invalid operation.")

# Create a number input for the first number.
number1 = st.number_input("Enter the first number:")

# Create a number input for the second number.
number2 = st.number_input("Enter the second number:")

# Create a dropdown menu for the mathematical operation.
operation = st.button(["+", "-", "*", "/", "^", "log", "sin", "cos", "tan", "sqrt"])

# Calculate the result of the mathematical operation.
result = calculate(operation, number1, number2)

# Display the result of the mathematical operation.
st.write("The result is", result)
