import smtplib, ssl
import os
from dotenv import load_dotenv


load_dotenv()

host = "smtp.gmail.com"
port = 465

username = os.getenv("GOOGLE_USERNAME")
password = os.getenv("GOOGLE_APP_PASSWORD")
receiver = os.getenv("GOOGLE_USERNAME")

context = ssl.create_default_context()

message = """
Subject: Test from portfolio app
Hi,
How are you?
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
