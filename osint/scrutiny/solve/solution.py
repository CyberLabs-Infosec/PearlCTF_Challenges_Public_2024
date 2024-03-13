import requests
import time
from pytube import YouTube

video_url = "https://youtu.be/TYbR_k9m6_c?si=bUzHZyHKN05mA5oq"

while True:
    try:

        yt = YouTube(video_url)
        thumbnail_url = yt.thumbnail_url


        thumbnail_data = requests.get(thumbnail_url)
        with open(f"./thumbnail_{time.time()}.jpg", "wb") as f:
            f.write(thumbnail_data.content)

        print("Thumbnail downloaded successfully.")

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(30)
