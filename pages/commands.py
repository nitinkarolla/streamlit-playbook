"""Other Commands page shown when the user enters the application"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import requests
from io import BytesIO

def main():
    st.title("Other Commands")

    # Display text
    st.header("Display Text")
    with st.echo():
        st.text("This is how text looks in streamlit.")

    # Markdown
    st.header("Markdown")
    with st.echo():
        # Note that emojis/latex are also supported
        st.markdown("This is how you **markdown**. :sunglasses:")

    # Latex
    st.write("Latex")
    with st.echo():
        st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)''')

    # Write
    st.header("Write")
    with st.echo():
        # Note that this command is like a swiss army knife. It has many functionalities
        # Number
        st.write(1234)
        # Dataframe
        st.write(pd.DataFrame({
            'Col 1': [1, 2, 3, 4],
            'Col 2': [12, 15, 16, 20]
        }))
        # Graph
        df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
        chart = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

        st.write(chart)

    # Code
    st.header("Code")
    with st.echo():
        st.code('''def hello():
    print("Hello, I am Nitin")''', language="python")

    # Dataframe
    st.header("Dataframe")
    with st.echo():
        # Note that the below can also be written as st.write(df). Also, width/height of the UI element can be altered
        # If the data is in Pandas format then styling can also be done
        st.dataframe(df, 300, 300)

    # Table
    st.header("Table")
    with st.echo():
        # The difference between a dataframe and table is that tables are static
        st.table(df)

    # JSON
    st.header("JSON")
    with st.echo():
        st.json({
            'one': '1',
            'two': '2',
            'some stuff': [
                'stuff 1',
                'stuff 2',
                'stuff 3',
                'stuff 5',
            ],
        })

    # Image
    st.header("Image")
    with st.echo():
        # Note that you can mention image width/caption/channels
        response = requests.get('https://images.unsplash.com/photo-1567960085854-41ea6238f516?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=743&q=80')
        img = Image.open(BytesIO(response.content))

        st.image(img, caption='The city that doesn\'t sleep', use_column_width=True)
        st.markdown("**Image Credit**")
        st.write("URL : https://unsplash.com/photos/vtryXDVa890")

    # Audio
    st.header("Audio")
    with st.echo():
        st.audio("https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg", format='audio/ogg')

        st.markdown("**Audio Credit**")
        st.write("URL: https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg")

    # Video
    st.header("Video")
    with st.echo():
        # Note that the only video format currently available is mp4
        st.video("https://pixabay.com/videos/download/video-6962_large.mp4", format = "mp4")

        st.markdown("**Video Credit**")
        st.write("URL : https://pixabay.com/videos/star-long-exposure-starry-sky-sky-6962/")