import os
import time
from datetime import datetime, timedelta
import googleapiclient.discovery
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload


def get_credentials():
    SCOPES = ['https://www.googleapis.com/auth/youtube']
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './creds/client_secret.json', SCOPES)
            creds = flow.run_console()

        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def set_thumbnail(youtube, video_id, thumbnail_path):
    request = youtube.thumbnails().set(
        videoId=video_id,
        media_body=MediaFileUpload(thumbnail_path)
    )
    response = request.execute()
    print("Thumbnail set successfully.")


def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    credentials = get_credentials()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    video_id = "TYbR_k9m6_c"
    default_thumbnail = "./pics/not_flag.jpeg"
    special_thumbnail = "./pics/flag.jpeg"
    spl_interval = 60
    norm_interval = 1800
    ext = 600
    while True:
        try:
            set_thumbnail(youtube, video_id, special_thumbnail)
            current_time = datetime.now() 
            print("Special thumbnail set at IST:",current_time.strftime("%Y-%m-%d %H:%M:%S"))
            print(f"Waiting for {spl_interval} seconds")
            time.sleep(spl_interval)
            set_thumbnail(youtube, video_id, default_thumbnail)
            current_time = datetime.now() 
            print("Default thumbnail set at IST:",current_time.strftime("%Y-%m-%d %H:%M:%S"))
            print(f"Waiting for {norm_interval} seconds")
            time.sleep(norm_interval)
        except Exception as e:
            print("An error occurred:", str(e))
            time.sleep(ext)

        if datetime.now() > credentials.expiry - timedelta(minutes=5):
            print("Refreshing credentials...")
            credentials = get_credentials()
            youtube = googleapiclient.discovery.build(
                api_service_name, api_version, credentials=credentials)

if __name__ == "__main__":
    main()
