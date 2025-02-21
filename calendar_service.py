import datetime
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Define Google Calendar API Scopes
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]
SERVICE_ACCOUNT_FILE = "service-account.json"

def create_calendar_event(summary, description, start_time, end_time,email):
    """Creates a Google Calendar event."""
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build("calendar", "v3", credentials=credentials)
    calendar_id="f111cd07bec27df6d9cda91aa9dcdb8c98375f1b56cc60c782cb4d8bf4abdf1a@group.calendar.google.com"

    event = {
        "summary": summary,
        "description": description,
        "start": {"dateTime": start_time, "timeZone": "UTC"},
        "end": {"dateTime": end_time, "timeZone": "UTC"},
        "reminders": {"useDefault": True},
    }
    try:
        event_result = service.events().insert(calendarId=calendar_id, body=event).execute()

        print("Event created:")
        print("ID:", event_result.get("id"))
        print("Summary:", event_result.get("summary"))
        print("Start:", event_result.get("start"))
        print("End:", event_result.get("end"))

        return event_result.get("htmlLink")
    except Exception as e:
        print(e)
        return None

# Test event creation
if __name__ == "__main__":
    event_link = create_calendar_event(
        summary="Test Event",
        description="This is a test event.",
        start_time="2025-02-21T10:00:00Z",
        end_time="2025-02-21T10:30:00Z",
        email="redietteklay8@gmail.com"
    )
    print("Event link:", event_link)