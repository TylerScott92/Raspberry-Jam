import RPi.GPIO as GPIO
import pygame
import time

# Variables
BUTTON_ONE = 12
BUTTON_TWO = 16

# GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_ONE, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(BUTTON_TWO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Pygame Initialization
pygame.mixer.init()

# Set Sound Files (put in same directory)
alien_file = "alien.wav" # Replace " " with .wav file
bark_file = "bark.wav"


# Begins Infinite Loop
while True:

	# Initialize Sound Files
	alien = pygame.mixer.Sound(alien_file)
	bark = pygame.mixer.Sound(bark_file)

	# Setup Input Variables
	input_one = GPIO.input(BUTTON_ONE)
	input_two = GPIO.input(BUTTON_TWO)

	# Determines Sound File Based On GPIO
	if input_one == 0:

		bark.play()
		print("Bark Playing")

		time.sleep(0.5)

	if input_two == 0:

		alien.play()
		print("Alien Playing")


	else:

		continue

	time.sleep(0.5)
