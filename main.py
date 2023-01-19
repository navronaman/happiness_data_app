import streamlit as st
import pandas as pd
import plotly.express as px
import functions as fn

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

index_x = options.index(option1)
index_y = options.index(option2)
x = fn.get_label(index_x)
y = fn.get_label(index_y)

x_ax, y_ax, fig = fn.get_data(valuex=x, valuey=y, op1=option1, op2=option2)

figure = px.scatter(data_frame=df, x=x, y=y, hover_data=["country"])

st.plotly_chart(fig)
st.plotly_chart(figure)

st.session_state





