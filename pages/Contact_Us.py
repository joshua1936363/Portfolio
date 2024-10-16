import streamlit as st
from pages.send_email import send_email


st.header("Contact Me")


with st.form(key="email_forms"):
    user_email = st.text_input("your email address")
    raw_message = st.text_area("your message here:")
    message = f"""\
subject = New email from {user_email}

From: {user_email}
{raw_message}
"""
    message = message + "\n" + user_email
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        st.info("your email was sent successfully")
