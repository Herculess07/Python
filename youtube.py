from pytube import YouTube
from tkinter import Tk

root = Tk()

# URL of the YouTube video
url = "https://www.youtube.com/watch?v=morCrJ5o47s"

# Creating a YouTube object
video = YouTube(url)

# Printing video title
print("Title:", video.title)

# Printing video description
print("Description:", video.description)

# Printing video duration
print("Duration:", video.length, "seconds")

# Printing available video streams
streams = video.streams.all()
for i, stream in enumerate(streams):
    print(i, "Resolution:", stream.resolution, "Type:", stream.mime_type)

# Downloading the video
stream = video.streams.get_by_itag('22')  # Corrected the parameter to a string

stream.download(output_path='./')


root.mainloop()