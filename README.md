# piano-youtube-tutorial-to-image-converter
this tool allows you to save those youtube piano synthesia tutorials where you have piano notes falling down as a single very tall image essentially like a spacial screenshot of the whole video 

just a disclaimer that this whole thing has been 100% vibe coded by a clueless person

how to get this to work:

\
step 0: (feel free to skip this if you're a programmer i'm trying to make this tutorial very noob friendly for people who are trying to learn the piano not computer science) get an ide 

i used "thonny" and it worked well but im sure others will work as well

just google download thonny and click on the official looking link and install it like normal

\
step 1: donwload a wholle lotta packages 

in thonny go to tools>manage packages then search "pillow" (no idea why its named like that but trust me) and press install

repeat for the following packages: "numpy" (might be already installed) "opencv-python" and "youtube_dl" (you actually might not need the last 2 but just like on christmas morning you can never have too many packages)

\
step 2: get gifcam

you will need to donwload a great little program called gifcam again just google it

i used version 5.1 because thats what i've had installed for years and i could never be bothered to update it but im sure newer versions will work too

\
step 3: create a 1 pixel tall gif of the video you want to save

open the youtube tutorial you want i will use this as an example:

https://www.youtube.com/watch?v=xmQcXspTIZc

set gif cam to match the fps of the video

right click on the yt video and open stats for nerds 

the bit where it says current/optimal res will say something like 640x338@30 the @30 bit tells you its a 30 fps video 

if its says 60 you might want to lower the video quality because dealing with huge gifs can be a pain 

also you might want to make the browser window where you have youtube open smaller to stop the gif from being too many pixels horizontally especially if you have a 4k monitor

in gifcam press the down arrow next to the rec button and set to fps to match the video, you might need to go into customization and add the fps option you need 

adjust the size of the gifcam window until its as wide as the video and only 1 pixel tall (you can see the size of your gif in the top left of the gifcam window)

with the video paused place the gifcam window over the piano keys in the video

with the gifcam window selected press enter to start recording (since the window is too small to actually press it with your mouse) you should see frame count and delay start to increase

smoothly move the gifcam window straight up until you reach about the middle of the video frame (this is to capture the keys in the final image)

play the youtube video

once the video stops click on the gifcam window and press enter to stop recording

save your gif ideally in the same folder as the program

you might want to change the save setting in gifcam to 20 colors or even monochrome in gifcam if your gif is getting too humongous but usually its not needed

\
step 3: open the pianogif2.py software

personally i do it in thonny

\
step 4: set up the program

change the gif_file parameter to whatever you saved your gif as

\
step 5: save and run the program

hopefully you see the message "Done!"

\
step 6: post processing

open the .png file the program generated in ms paint

you might notice it looks quashed vertically, well... its free software so you get what you paid for...

stretch it vertically 

i tend to zoom out, expand the canvas vertically, ctrl+a, resize, untick maintain aspect ratio, change vertical to 200 or 300 or 400% or whatever you want honestly the world is our oyster it belongs to us all

while you're in ms paint you can also crop out and resize the image as you please

\
~finished

\
faq:

Q: why does this exist?

A: it saved you the hassle of having to learn to read sheet music also scrubbing through youtube videos can be annoying expecially on a phone where its not very accurate and sometimes the video has to reload

also less data usage and distractions meaning you're more likely to actually play the piano instead of doomscrolling 1000 youtube shorts

plus you can see the whole song at once instead of just a few notes and you can scroll through it as fast or slow as you want and its just more intuitive to scroll vertically instead of horizontally


Q: what happens if i accidentally make the gif more than 1 pixel tall

A: no idea im honestly too terrfied to try just like dont do that 


Q: what is ignore.txt on this github page?

A: so the original idea was that the software donwloads the video automatically and makes the final image without having to first create the gif but that didn't work and geve me an error message so i gave up

and went with the gif idea instead but i thought i would upload the original code here anyway just in case anyone wants to try to make it work
