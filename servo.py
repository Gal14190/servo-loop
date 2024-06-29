# GAL ASHKENAZI [28/06/2024]
# servo.py

import time
from adafruit_servokit import ServoKit

MAX_CHANNELS = 16

kit = ServoKit(channels=MAX_CHANNELS)

def init():
	for s in range(0, MAX_CHANNELS):
		kit.servo[s].set_pulse_width_range(500, 2500)

	kit.servo[0].set_pulse_width_range(1000, 2500)

	kit.servo[MAX_CHANNELS - 1].angle = 180

def rotat(angle):
	for s in range(0, MAX_CHANNELS - 1):
		kit.servo[s].angle = angle

def wait():
	time.sleep(0.6)

def main():
	while(True):
		rotat(180)
		wait()
		rotat(0)
		wait()

if __name__ == '__main__':
	init()	# init servos
	main() # run

