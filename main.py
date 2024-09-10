"""module to change wallpaper"""
import ctypes
import playsound
import os 
import sys 
script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 

WALLPAPER_PATH = f"{script_directory}/assets/trumpshooting.webp"
# 0: Center, 1: Stretch, 2: Tile, 6: Fit
WALLPAPER_STYLE = 1
# Set the wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, WALLPAPER_STYLE)
print("part 1 successful")

#Play sound
playsound.playsound("assets\\buildawall.mp3")
print("part 2 successful")
