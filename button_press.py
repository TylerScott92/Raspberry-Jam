import RPi.GPIO as GPIO
import time


# Variables
RED = 12
YELLOW = 16
BUTTON = 18

# Set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)

# Turns on red light while button is pressed
while True:

	input = GPIO.input(BUTTON)

	if input == 0:
		GPIO.output(RED, GPIO.HIGH)
		print("Red On")

	else:
		GPIO.output(RED, GPIO.LOW)

	time.sleep(0.3)
