import streamlit as st
import pandas as pd

name = st.text_input("Enter the Text")
age = st.slider("Enter the age" , 0,100,25)

options = ["Java" , "Python" , "Javascript" , "C"]
selectedOption = st.selectbox("Select the Language" , options)


if(name):
    st.write(f"Hello {name}")
    st.write(f"Your age is {age}")
    st.write(f"Selected option is {selectedOption}")


file = st.file_uploader("Upload the file" , type=["csv"])

data_set = pd.read_csv(file)

if file is not None:
    st.write(data_set)
