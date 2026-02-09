from pytube import YouTube

  # :(


def download_video(url):
    try:
        yt = YouTube(url)
        print(f"Downloading: {yt.title}")

        # start download
        yt.download() # Corrected typo from .downlad()
        print("Download completed...")

    except Exception as e:
        print(f"An error occurred: {e}")

# Use a real YouTube video URL here
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # Example: Rick Astley - Never Gonna Give You Up
download_video(video_url)

