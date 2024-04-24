import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()

st.header("Contact Us")

username = os.getenv('GOOGLE_USERNAME')
password = os.getenv('GOOGLE_APP_PASSWORD')

print(username)
print(password)


with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message here...")
    button = st.form_submit_button()

    if button:
        print(button)
        print("I was pressed")