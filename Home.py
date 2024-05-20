import streamlit as st
import pandas as pd
from PIL import Image
import os


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/kit_photo.jpg", width=256)

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

content2 = ("Below you will find some of the apps I have built with Python.  "
            "Feel free to contact me!")
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")
df["source url"] = df["source url"].astype(str)
df["app url"] = df["app url"].astype(str)

with col3:
    for index, row in df[:11].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        image = "images/" + row["image"]
        st.image(image, width=256)

        source_link = ""
        if (pd.notna(row['source url'])
                and row['source url'] != 'nan'
                and row['source url'].strip() != ''):
            source_link = f"[Source]({row['source url']})"

        app_link = ""
        if (pd.notna(row['app url'])
                and row['app url'] != 'nan'
                and row['app url'].strip() != ''):
            app_link = f"[App]({row['app url']})"

        if source_link or app_link:
            st.markdown(
                f"<span style='font-size:20px;'>{source_link}"
                f"&nbsp;&nbsp;&nbsp;&nbsp;{app_link}</span>",
                unsafe_allow_html=True
            )

        else:
            st.write("COMING SOON")

with col4:
    for index, row in df[11:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        image = "images/" + row["image"]
        st.image(image, width=256)

        source_link = ""
        if (pd.notna(row['source url'])
                and row['source url'] != 'nan'
                and row['source url'].strip() != ''):
            source_link = f"[Source]({row['source url']})"

        app_link = ""
        if (pd.notna(row['app url'])
                and row['app url'] != 'nan'
                and row['app url'].strip() != ''):
            app_link = f"[App]({row['app url']})"

        if source_link or app_link:
            st.markdown(
                f"<span style='font-size:20px;'>{source_link}"
                f"&nbsp;&nbsp;&nbsp;&nbsp;{app_link}</span>",
                unsafe_allow_html=True
            )

        else:
            st.write("COMING SOON")


