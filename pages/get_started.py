"""Overview page shown when the user enters the application"""

import streamlit as st
import pandas as pd
import numpy as np


def main():
    #### Getting Started ####   
    st.title("Getting Started")
    st.video("https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/udacity_car_demo-2.mp4",format = "mp4")

    st.write("One can install streamlit using PIP and test out the hello world app by running the command 'streamlit hello' from your \
        terminal")

    st.text("$ pip install streamlit")
    st.text("$ streamlit hello")

    st.write("To start building an app create a python file and import \
        and start coding. It is recommended to code and view the changes \
        parallely together.")

    st.text("$ import streamlit as st")

    st.write("Working with streamlit is simple")
    st.text("$ streamlit run your_script.py [-- script args]")
    st.write("As soon as you run the script as shown above, a local Streamlit \
        server will spin up and your app will open in a new tab on your default \
        web browser.")
    st.write("Streamlit allows you to work in a fast interactive loop: you type \
        some code, save it, try it out live, then type some more code, save it, \
        try it out, and so on until you’re happy with the results.")

    st.write("Also you can pass a URL to streamlit run")
    st.text("$ streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/app.py")

    #### Text and Data Section ####    
    st.title("Adding Text and Data")

    st.write("Adding a title is as simple as this")
    with st.echo():
        st.title("This is a not a title")

    st.write("Write command from streamlit is considered as Streamlit's 'Swiss\
            Army knife'. You can pass anything to st.write() : text, data,     \
            Matplotlib figures, Altair charts etc")

    with st.echo():
        st.write("Here's our first attempt at using data to create a table:")
        st.write(pd.DataFrame({
            'first column': [1, 2, 3, 4],
            'second column': [10, 20, 30, 40]
        }))

    #### Magic #### 
    st.title("Using Magic")
    st.write("Any time that Streamlit sees a variable or a literal value on its own line, it automatically writes that to your app using st.write()")
    
    with st.echo():
        """
        Here's our first attempt at using data to create a table:
        """

        df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
        })

        df
    st.write(df)
    st.write("Note : Magic is not available inside a function")

    #### Charts and Maps ####
    st.title("Drawing Charts and maps")
    st.write("You can easily add a line chart to your app with st.line_chart().")
    
    with st.echo():
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

        st.line_chart(chart_data)
    
    st.write("With st.map() you can display data points on a map.")

    with st.echo():
        map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [38.02, -78.47],
        columns=['lat', 'lon'])

        st.map(map_data)