from pytube import YouTube, Playlist
import os
import sys

from config import OUTPUT_FOLDER

if __name__ == "__main__":
    playlist = Playlist(sys.argv[1])

    for url in playlist:
        print(f"Downloading {url}")
        mp4_file = (
            YouTube(url).streams.filter(only_audio=True).first().download(OUTPUT_FOLDER)
        )

        # save the file as mp3
        base, ext = os.path.splitext(mp4_file)
        mp3_file = base + ".mp3"
        os.rename(mp4_file, mp3_file)

    print("All Done")
