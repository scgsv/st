import streamlit as st
import random
import time

st.title("Streamlit Widget Showcase")

# Text Input widget
name = st.text_input("Enter your name", "Type Here")

# Checkbox widget
if st.checkbox("Show greeting"):
    st.write("Hello, ", name)

# Radio button widget
activity = st.radio("Choose your favorite activity", ("Sleeping", "Eating", "Playing"))
if activity == "Sleeping":
    st.write("Zzz...")
elif activity == "Eating":
    st.write("Yum!")
else:
    st.write("Let's play!")

# Selectbox widget
genre = st.selectbox("Choose your favorite genre", ("Comedy", "Drama", "Action"))
if genre == "Comedy":
    st.write("Laugh it off!")
elif genre == "Drama":
    st.write("Feel the emotions!")
else:
    st.write("Action-packed!")

# Multi-select widget
interests = st.multiselect("Select your interests", ("Sports", "Music", "Travel", "Reading"))
st.write("Your interests are: ", interests)

# Slider widget
level = st.slider("What is your skill level?", 1, 10)
st.write("Your skill level is: ", level)

# Progress bar widget
progress = st.progress(0)
for i in range(100):
    time.sleep(0.02)
    progress.progress(i + 1)

# Text area widget
text = st.text_area("Type something", "Write here")
st.write("You wrote: ", text)

# Date picker widget
date = st.date_input("Pick a date", time.time())
st.write("The selected date is: ", date)

# Time picker widget
time = st.time_input("Pick a time", datetime.time(12, 0))
st.write("The selected time is: ", time)

# Button widget
if st.button("Generate random number"):
    st.write("Random number: ", random.randint(0, 100))

# Balloons widget
add_balloon = st.sidebar.button("Add a balloon")
if add_balloon:
    st.balloons()
