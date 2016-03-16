import os

os.system("sudo cat /sys/class/backlight/rpi_backlight/brightness > brightness.txt")

with open('brightness.txt') as f:
	for i in xrange(1):
		value = f.readline().rstrip()

		if 255 == int(value):
			os.system("echo 25 | sudo tee /sys/class/backlight/rpi_backlight/brightness")
			print "Display abdunkeln"
		else:
			os.system("echo 255 | sudo tee /sys/class/backlight/rpi_backlight/brightness")
			print "Display erhellen"