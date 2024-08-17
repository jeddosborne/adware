"""module to change wallpaper"""
import ctypes
import playsound

WALLPAPER_PATH = "C:\\Users\\jeddo\\Documents\\CODE\\adware-1\\assets\\trumpshooting.webp"
# 0: Center, 1: Stretch, 2: Tile, 6: Fit
WALLPAPER_STYLE = 1
# Set the wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, WALLPAPER_STYLE)
print("part 1 successful")

#Play sound
playsound.playsound("C:\\Users\\jeddo\\Documents\\CODE\\adware-1\\assets\\buildawall.mp3")
print("part 2 successful")
