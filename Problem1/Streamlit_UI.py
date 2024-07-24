########################   UseCase - 1 ##############################
from dotenv import load_dotenv
import streamlit as st
import requests
import json
import os
import requests

# Function to send email
def send_email(receiver_emails, subject, body):
    url = os.getenv('MAILLINK')
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "receiver_emails": receiver_emails,
        "subject": subject,
        "body": body
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response

# Function to post to LinkedIn
def post_linkedin(title, image_url, text_content):
    url = os.getenv('LINKEDIN')
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "title": title,
        "image_url": image_url,
        "text_content": text_content
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response

# Streamlit UI
st.title('HR Interface for Email and LinkedIn Post')

# Employee Notification Section
st.header('Notify Employee')
receiver_emails = st.text_input('Receiver Emails (comma separated)', 'Employee Mail')
subject = st.text_input('Subject', 'Subject')
body = st.text_area('Body', 'Body')
if st.button('Send Email to Employee'):
    receiver_emails_list = [email.strip() for email in receiver_emails.split(',')]
    email_response = send_email(receiver_emails_list, subject, body)
    if email_response.status_code == 200:
        st.success(f"Email sent status: {email_response.json().get('sent', False)}")
    else:
        st.error(f"Failed to send email. Status code: {email_response.status_code}")
        st.error(email_response.text)

# Manager Notification Section
st.header('Notify Manager of Selected Employee')
manager_emails = 'sanjay.s@goml.io'
manager_subject = st.selectbox('Manager Subject', ['Selected', 'Rejected'])
manager_body = st.text_area('Email', 'Candidate Details')
if st.button('Send Email to Manager'):
    manager_emails_list = [manager_emails]
    manager_email_response = send_email(manager_emails_list, manager_subject, manager_body)
    if manager_email_response.status_code == 200:
        st.success(f"Email sent status: {manager_email_response.json().get('sent', False)}")
    else:
        st.error(f"Failed to send email. Status code: {manager_email_response.status_code}")
        st.error(manager_email_response.text)

# LinkedIn Section
st.header('Post to LinkedIn')
title = st.text_input('Title', 'Enter Title')
image_url = st.text_input('Image URL', 'https://i.pinimg.com/originals/cb/37/5e/cb375e56ea17907217a0b970e8eef870.png')
text_content = st.text_area('Text Content', 'Content')
if st.button('Post to LinkedIn'):
    linkedin_response = post_linkedin(title, image_url, text_content)
    if linkedin_response.status_code == 200:
        st.success(f"LinkedIn post status: {linkedin_response.json().get('status', 'failed')}")
    else:
        st.error(f"Failed to post to LinkedIn. Status code: {linkedin_response.status_code}")
        st.error(linkedin_response.text)
