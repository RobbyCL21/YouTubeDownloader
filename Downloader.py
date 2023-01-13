# IMPORTING NECESSARY 
# FOR PYTUBE USE PIP3 INSTALL PYTUBE
from pytube import YouTube
from sys import argv

link = argv[1] # IN CMD OR COMMAND LINE U WILL PUT UR PYTHON FILE ( which is argv [0], and a youtube link which is argv[1])
# WE WANT THE YOUTUBE LINK
youtube_video = YouTube(link) # TAKE THE VIDEO FROM YOUTUBE WITH THE LINK UVE GIVEN

print("Title: ", youtube_video.title) # HERE WE CAN TEST SOME BUILT IN YouTube LIBRARY COMMANDS LIKE TITLES OR VIEWS

youtube_download = youtube_video.streams.get_highest_resolution() # GET THE HIGHEST RESOLUTION IS A FUNCTION BUILT IN TO GET THE HIGHEST 4K

youtube_download.download('/Users/robby/Videos/YouTube videos') # YOU PUT THE LOCATION OF WHERE U WANT THE VIDEO TO GO

print('Download has worked!') # PRINTING THIS TO KNOW WHEN I CAN CLOSE THE CODE BECAUSE IT IS DONE DOWNLOADING

# WRITE IN YOUR COMMAND LINE:
# python3 Downloader.py "(Your video you want to download)"