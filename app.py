import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
SERVICE_ACCOUNT_FILE = 'refresh-afda8-firebase-adminsdk-yqut1-534f470cdc.json'  # Path to the JSON key

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

def send_push_notification(platform, topic, title, message):
    # Prepare the FCM API URL
    url = f"https://fcm.googleapis.com/v1/projects/{project_id}/messages:send"

    # Set up request headers
    access_token = _get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Create the payload based on the platform (iOS or Android)
    if platform.lower() == "ios":
        # Payload for iOS
        payload = {
            "message": {
                "topic": topic,
                "data": {
                    "title": title,
                    "body": message
                },
                "notification": {
                    "title": title,
                    "body": message
                },
                "apns": {
                    "payload": {
                        "aps": {
                            "content-available": 1
                        }
                    }
                }
            }
        }
    elif platform.lower() == "android":
        # Payload for Android
        payload = {
            "message": {
                "topic": topic,
                "data": {
                    "title": title,
                    "body": message
                }
            }
        }
    else:
        print("Invalid platform. Choose either 'ios' or 'android'.")
        return

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print(f"Notification successfully sent to {platform} on topic {topic}")
    else:
        print(f"Error sending notification: {response.status_code}, {response.text}")

if __name__ == "__main__":
    platform = input("Enter the platform (ios or android): ")
    topic = input("Enter the topic (e.g., 'all' or 'ios'): ")
    title = input("Enter the notification title: ")
    
    print("Enter the notification message (type 'END' on a new line to finish):")
    
    # Сбор многострочного сообщения
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    
    message = "\n".join(lines)  # Собираем все строки в одно сообщение
    
    send_push_notification(platform, topic, title, message)