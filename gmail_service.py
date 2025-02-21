import os
import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def send_email(to, subject, message):
    """Sends an email using Gmail API."""
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    service = build("gmail", "v1", credentials=creds)

    # Create email message
    msg = MIMEText(message)
    msg["to"] = to
    msg["subject"] = subject
    raw_msg = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")

    # Send email
    service.users().messages().send(userId="me", body={"raw": raw_msg}).execute()
    print(f"Email sent to {to}")

# Test the function
if __name__ == "__main__":
    send_email("redietteklay8@gmail.com", "Order Update", "Your order has shipped!")
