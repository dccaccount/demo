import streamlit as st

st.title("Addition Calculator")

num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

if st.button("Add"):
    result = num1 + num2
    st.success(f"The sum is: {result}")