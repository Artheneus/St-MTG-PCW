from ast import With
import streamlit as st

st.header("This is substraction page")

a1, a2 = st.columns(2)
b1 = st.columns(1)


with a1:
    num1 = st.number_input(
        "Number 1",
        max_value=1e8,
    )

with a2:
    num2 = st.number_input(
        "Number 2",
        max_value=1e8,
    )

total = num1 - num2
st.write(total)