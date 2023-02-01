from sense_hat import SenseHat
import time

# the SenseHat that we're using to get the value
sense = SenseHat()#

# some colours for display
dry = [255, 255, 0]
comfortable = [255, 255, 255]
wet = [0, 0, 255]

# look forever
while True:
	# get the humidity
	humidity = sense.get_humidity()

	# if dry
	if humidity <= 30:
		sense.clear(dry)
		sense.show_message("Air too dry, get a humidifier", scroll_speed=.1, text_colour = wet, back_colour=dry)
	elif 30 < humidity and humidity < 60:
		sense.clear(comfortable)
		sense.show_message("Air perfect", scroll_speed=.1, text_colour=wet, back_colour=comfortable)
	else:
		sense.clear(wet)
		sense.show_message("Air too wet, dehumidify!", scroll_speed=.1, text_colour=comfortable, back_colour=wet)

	# print dew point
	dew_point = sense.get_temperature() - ((100 - humidity)/5)
	print("Dew point is: %s"%(dew_point))
	# sleep for a second
	time.sleep(1)
