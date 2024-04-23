import streamlit as st


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/kit_photo.jpg")

with col2:
    st.title("Kitwana Akil")
    content = """
    Hi, I am Kitwana Akil.  I am a programmer and digital marketer.
    I have a Bachelors Degree in Information Technology.  I have 
    achieved certifications in a variety of different technologies
    including MSCE and Java.  I have worded for several companies as
    a mobile developer.  I run my own web server to host
    my websites, APIs, and web applications.  My current focus is 
    python and machine learning.
    """
    st.info(content)

content2 = "Below you will find some of the apps I have built with Python.  Feel free to contact me!"
st.write(content2)

