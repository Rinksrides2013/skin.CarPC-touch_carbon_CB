import os

os.system("echo 255 | sudo tee /sys/class/backlight/rpi_backlight/brightness");