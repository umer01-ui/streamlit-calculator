import streamlit as st
st.title("--SIMPLE STUDENT CALCULATOR--")
"=========================================================="
num1=st.number_input("ENTER FIRST NUMBER", )
num2=st.number_input("ENTER SECOND NUMBER", )


operation=st.selectbox(
    "SELECT OPERATION",
    ("ADDITION", "SUBTRACTION", "MULTIPLICATION", "DIVISION")
)

def calculate(num1, num2, op):
    if op=="ADDITION":
        return num1+num2
    elif op=="SUBTRACTION":
        return num1-num2
    elif op=="MULTIPLICATION":
        return num1*num2
    elif op=="DIVISION":
        if num2==0:
            return "ERROR INSERT NUMBER GREATER THAN  0"
        return num1/num2

if st.button("CALCULATE"):
    result=calculate(num1, num2, operation)
    st.success(f"RESULT: {result}")
