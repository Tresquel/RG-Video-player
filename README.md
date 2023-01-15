# What is this?
This is the video converter and server for my Retro Gadgets project.

# What does it do?
- Converts the video frames into a format that the gadget can understand
- Runs a server where the gadget can access the file from

# What do I need?
- [Python 3.10+](https://www.python.org/)
- [FFmpeg](https://ffmpeg.org/)
  
# How do I use this?
- Put a gif or video in the `frames` folder
- Go into the `frames` folder with CMD or Powershell
- Run `ffmpeg -i FILENAME.EXTENSION -s 65x36 -vsync 0 %d.png` (Change `FILENAME` to the filename and `EXTENSION` to match the video/gif)
- Run `convert.py`
- Run `server.py`
- That's it!
