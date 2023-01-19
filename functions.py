import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("happy.csv")


def get_data(valuex, valuey, op1, op2):
    x_axis = df[valuex]
    y_axis = df[valuey]
    color = df["happiness"]
    hover = df["country"]

    figure = px.scatter(x=x_axis, y=y_axis,
                        labels={"x": op1, "y": op2,
                                "hover_data_0": "Country",
                                "color": "Happiness"},
                        color=color, hover_data=[hover])

    return x_axis, y_axis, figure


def get_label(index):
    oglist = df.columns
    return oglist[index+1]


if __name__ == "__main__":
    x = get_label(1)
    print(x)
