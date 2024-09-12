# FCM Push Notifications in Python

This project demonstrates how to send push notifications to devices subscribed to Firebase Cloud Messaging (FCM) topics using the **FCM HTTP v1 API**. It leverages the **Google Auth** library for OAuth 2.0 authentication to generate an access token required for FCM API requests.

## Requirements

Before running the script, ensure you have the following:

- Python 3.x
- A Firebase project with Cloud Messaging API enabled.
- A service account JSON key file from your Firebase project.
- Installed dependencies (listed below).

### Prerequisites

- **Service Account JSON Key**:
  Generate a service account key from your Firebase project and download the JSON file:
  
  1. Go to the **Firebase Console**.
  2. Navigate to **Project Settings** → **Service Accounts**.
  3. Click **Generate New Private Key** to download the JSON file.

- **Enable FCM API**:
  Ensure the **Firebase Cloud Messaging API** is enabled in the [Google Cloud Console](https://console.cloud.google.com/apis).

## Installation

1. Clone this repository or download the script.

2. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Place the JSON file with your Firebase service account key in the project folder and update the `SERVICE_ACCOUNT_FILE` path in the script.

## Usage

1. **Edit the script**:
   Update the `SERVICE_ACCOUNT_FILE` variable in the Python script to point to your JSON file:

   ```python
   SERVICE_ACCOUNT_FILE = 'path/to/your-service-account.json'
   ```

2. **Run the script**:
   The script will prompt you to input a topic, notification title, and message body:

   ```bash
   python3 app.py
   ```

3. **Input details**:
   - **Platform**: Select whether the notification will be sent to iOS or Android.
   - **Topic**: Enter the FCM topic.
   - **Title and Message**: Provide the title and message for the notification. For the message, you can enter multiple lines, ending with “END” to signal the completion of input.

4. **Example Input**:
   ```
   Enter the platform (ios or android): ios
   Enter the topic (e.g., 'all' or 'ios'): ios
   Enter the notification title: New products!
   Enter the notification message (type 'END' on a new line to finish):
   Good morning, dear customers!
   We invite you to try new products from a new supplier!
   END
   ```

5. **Notification Delivery**:

   - For **iOS**, both data and notification payloads are used to ensure the message shows up in the notification shade and can be processed in the app.
   - For **Android**, only the data payload is used, as Android processes both notifications and data differently.

## License

This project is licensed under the MIT License.

### Notes
- Make sure to use the correct service account.
- The service account must have permissions to send messages through Firebase Cloud Messaging.
