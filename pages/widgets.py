"""Widgets page explores the different widgets that can be added"""

import streamlit as st
import datetime
import pandas as pd

def main():
    st.title("Widgets")
    st.write("With widgets, Streamlit allows you to bake interactivity directly into your apps with buttons, sliders, text inputs, and more.")

    # First widget - Button
    st.header("Button")
    with st.echo():
        if st.button('Please click me'):
            st.write('You listened to me.')
        else:
            st.write("Click above")

    # Second widget - Checkbox
    st.header("Checkbox")
    with st.echo():
        yes = st.checkbox("Select me")

        if yes:
            st.write("You are the chosen one.")

    # Third widget - Radio
    st.header("Radio button")
    with st.echo():
        # Note that the options can be a numpy array/pandas Series/pandas Dataframe(first column taken)
        rad_question = st.radio("Are humans the original machine learning model?", ("Yes", "No", "Let's train a model."
                                                                                    ))

        if rad_question == "Yes":
            st.write("You maybe right.")
        elif rad_question == "No":
            st.write("Then who is it?")
        elif rad_question == "Let's train a model.":
            st.write("Is a human supposed to do it?")

    # Fourth widget - Selectbox
    st.header("Select box")
    with st.echo():
        # Note that the options can be a numpy array/pandas Series/pandas Dataframe(first column taken)
        sel_question = st.selectbox("Who is the leader of the Justice League?", ("Flash", "Batman", "Aquaman",
                                                                                 "Green Lantern", "Wonder Woman",
                                                                                 "Superman", "Cyborg",
                                                                                 "Martian Manhunter",
                                                                                 "I don't know what is the Justice"
                                                                                 " League"))
        if sel_question == "Batman":
            st.write("Yes, in truth it is Batman.")
        elif sel_question == "Superman":
            st.write("That is what everyone is told.")
        elif sel_question == "I don't know what is the Justice League":
            st.write("How can you not know? FYI. Superman is the answer.")
        else:
            st.write("That is not right. Try again.")

    # Fifth widget - Multiselect
    st.header("Multiselect")
    with st.echo():
        # Note that the options can be a numpy array/pandas Series/pandas dataframe(first column taken)
        # Also, you can select multiple options by default
        multi_sel_question = st.multiselect("What is your favorite dish?", ["Pancake", "Fried Eggs", "Hashbrowns"],
                                            ["Pancake"])

        st.write("I see that you like ", multi_sel_question)

    # Sixth widget - Slider
    st.header("Slider")
    with st.echo():
        # Sliders support int/float/date/time/datetime
        values = st.slider("How much are you enjoying work from home?", 0, 100, 20)

        st.write("On a scale of 0-100, you seem to be enjoying work from home around ", values)

    # Seventh widget - Text Input
    st.header("Text Input")
    with st.echo():
        # Note that you can mention the maximum number of characters that can be entered
        movie_title = st.text_input("What is your favorite movie?", "Inception")

        st.write('Wow!  \"', movie_title, '\" is a really good movie.')

    # Eighth widget - Number Input
    st.header("Number Input")
    with st.echo():
        # Note that you can mention the min value/max value/step count/display format
        num_input = st.number_input("How many countries have you travelled?", 1, 50, 1)

        st.write("You have travelled to ", num_input, " countries. That is very cool.")

    # Ninth widget - Text Area
    st.header("Text Area")
    with st.echo():
        # Note that you can mention height of box/max characters
        my_text = st.text_area("Write about your current activity", "I am currently building the widget section of the "
                                                                    "Playbook using streamlit. So far it has been quite "
                                                                    "fun. I am really enjoying it. Hope you guys enjoy "
                                                                    "it too.")
        st.write("Current Activity : ", my_text)

    # Tenth widget - Date Input
    st.header("Date Input")
    with st.echo():
        # Note that you can mention the minimum/maximum selectable date
        dat_inp = st.date_input("What is your date of birth?", datetime.date(2020, 1, 22))

        st.write("So it's ", dat_inp)

    # Eleventh widget - Time Input
    st.header("Time Input")
    with st.echo():
        tim_inp = st.time_input("What time do you wake up everyday?", datetime.time(7, 45))

        st.write("I will set an alarm for ", tim_inp)

    # Twelfth widget - File Uploader
    st.header("File Uploader")
    with st.echo():
        # Note that you can mention the file type and encoding
        st.set_option('deprecation.showfileUploaderEncoding', False)
        load_file = st.file_uploader("Upload a CSV file", type="csv")

        if load_file is not None:
            data = pd.read_csv(load_file)
            st.write("The data you uploaded is ")
            st.write(data)

    # Thirteenth widget - Color Picker (Beta version)
    st.header("Color Picker (Beta version)")
    with st.echo():
        # Note that this is in it's beta testing version. The colors are in HEX format
        color = st.beta_color_picker("Pick a color", "#00f900")

        st.write("The color you picked is ", color)
