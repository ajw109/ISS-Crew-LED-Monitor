import requests
from gpiozero import LEDBarGraph
from time import sleep

# Create an LED Bar Graph containing all the GPIO pins you are using
leds = LEDBarGraph(2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

# Use requests module to load data into Python
url = "https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json"

while True:
	# Use requests module to load data into Python
	r = requests.get(url)
	data = r.json()
	
    # Pull current number of people in the ISS
	people = data['number']
	
	leds.off()
	leds.value = people/10 # Light number of LEDs equal to the number of people in the ISS
	sleep(60) # Wait 60 seconds before running again