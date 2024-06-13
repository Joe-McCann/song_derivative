Welcome to this project to take a derivative of a song using Fourier Transforms. Big shout out to [TokieSan](https://www.tiktok.com/@tokiesan) who wrote this code used here to process the audio.

Please note that in order to use this project you should have [ffmpeg](https://ffmpeg.org/). 

In the event that you want to download the audio from a Youtube video from the python script, you will
need the package [Youtube DLP](https://github.com/yt-dlp/yt-dlp). If you already have a `wav` file though,
this is uneccessary. 

I am running Python version `3.10.6`, install packages using `pip3 install -r requirements.txt`. Or just do it yourself, there aren't many packages you need.

**Note** that all audio must be `wav` files in order to make this work.

## How to Use

If you want to download a video from youtube using yt-dlp, just put the URL to the youtube video into the 
`"https://www.youtube.com/watch?v=dQw4w9WgXcQ"` variable. The variable `SONG_FILE` represents the filename that the
song will be downloaded to. The file `OUTPUT_FILE` represents the file the derivative will be put into.