import streamlit as st
import pandas as pd

df = pd.read_csv("happy.csv")

st.title("In search for Happiness")

options = list(df.columns[1:])
for index, i in enumerate(options):
    if i == "gdp":
        options[index] = "GDP"
    elif i != "gdp":
        i = i.replace("_", " ")
        i = i.title()
        options[index] = i

option1 = st.selectbox("Select the data for x-axis", key="xaxis",
                       options=options, index=0)

option2 = st.selectbox("Select the data for y-axis", key="yaxis",
                       options=options, index=1)

subhead = f"{option1} and {option2}"
st.subheader(subhead)




