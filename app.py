import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
SERVICE_ACCOUNT_FILE = 'path/to/your-service-account.json'  # Path to the JSON key

def _get_access_token():
    """Retrieve a valid access token."""
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    request = Request()
    credentials.refresh(request)
    return credentials.token

# Load project_id from the JSON key file
with open(SERVICE_ACCOUNT_FILE) as f:
    firebase_creds = json.load(f)
project_id = firebase_creds['project_id']  # Extract project_id

def send_push_notification(topic, title, message):
    # Prepare the FCM API URL
    url = f"https://fcm.googleapis.com/v1/projects/{project_id}/messages:send"

    # Set up request headers
    access_token = _get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Create the payload for the notification
    notification_body = {
        "message": {
            "topic": topic,
            "notification": {
                "title": title,
                "body": message
            }
        }
    }

    response = requests.post(url, headers=headers, json=notification_body)
    
    if response.status_code == 200:
        print(f"Notification successfully sent to topic {topic}")
    else:
        print(f"Error sending notification: {response.status_code}, {response.text}")

if __name__ == "__main__":
    topic = input("Enter the topic (e.g., 'all' or 'ios'): ")
    title = input("Enter the notification title: ")
    message = input("Enter the notification message: ")

    send_push_notification(topic, title, message)