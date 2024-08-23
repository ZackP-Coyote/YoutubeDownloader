from pytube import YouTube
from sys import argv

# Ask the user for input
link = input("Enter the YouTube video link: ")
# Example: python main.py https://www.youtube.com/watch?v=9bZkp7q19f0

# Create a YouTube object
yt = YouTube(link)

# Get the highest resolution video stream
ys = yt.streams.get_highest_resolution()

# Download the video
print("Title: ", yt.title)
print("Downloading...")

# Save the video to the specified directory
ys.download('/Users/user/Videos/YTDownloads')

print("Download completed!")
