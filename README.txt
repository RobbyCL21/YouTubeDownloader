Welcome to my YouTube Downloader

I have created this YouTube downloader for when I go on vacations and would like to watch a video.
These video's need WiFi so the best way to watch them is by downloading them before I leave the house.

So what happens in this code, you may ask?

Step 1: The imports

# PYTUBE
Pytube is a library that we will need for connecting to YouTube 

This needs some pip installing so go in your cmd or terminal and write the following code:
pip3 install pytube

After this installation is done you should be fine to import the following

# YouTube

This is going to be a necessary import when we want to connect a link and YouTube library together to find and download it.
This library will have a few things like "title, views and more" 

# argv

This code is run in a cmd or in the terminal where u run this program.
When writing the code u name the program name and the link of your youtube video
With this we can make sure we grab the right value 

Step 2: get the link

This code is run in a cmd or in the terminal where u run this program.
When writing the code u name the program name and the link of your youtube video as mentioned above
by using "argv[1]" we say the 2nd position we wrote 
So when writing "Downloader.py "link"" the link is the second position or in coding language this is 1 since it starts at 0

Step 3: Connecting to YouTube

then we connect to youtube with the link thats been given , so we can get the details of the video later

Step 4: Get the details u want to be printed

We just print of the details we want they are not necessary but i print them to make sure things work and the right
video is being processed and downloaded

Step 5: Download it!

Th YouTube library has a download function so you write the name of your variable.download()
inbetween those (), you write the location u want the code send the video towards and there u go!

Step 6: Run the code in your terminal

Then u go to the terminal and run this code:
python3 Downloader.py "link" and video will be downloaded for you

Edit:

I've created a function out of it, with a parameter of the link 
The link being a parameter means that i give the function the action to run only when given a parameter
Parameter being the link u want to download , code still runs the same just that the code rn is inside of a def / function