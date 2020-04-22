import RPi.GPIO as GPIO
import pygame
import time

class Buttons:

	# Global list to hold all sound files
	notes = []

	def __init__(self):

		print("Button Constructor")

	def callSound(self):

		# Mixer initialization
		pygame.mixer.init()

		# Assign names to variables
		alien_file = "alien.wav"
		bark_file = "bark.wav"
		bell_file = "bell.wav"

		# Assign file to mixer 
		alien = pygame.mixer.Sound(alien_file)
		bark = pygame.mixer.Sound(bark_file)
		bell = pygame.mixer.Sound(bell_file)

		# Put files into global list
		global notes
		notes = [alien, bark, bell]


	def buttonSetup(self):

		# Variables
		BUTTON_ONE = 12
		BUTTON_TWO = 16
		BUTTON_THREE = 18

		# Put GPIO pins in list
		button_list = [BUTTON_ONE, BUTTON_TWO, BUTTON_THREE]

		# Access notes from global variable
		global notes
		alien = notes[0]
		bark = notes[1]
		bell = notes[2]

		# GPIO Setup
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		for i in range (3):
			GPIO.setup(button_list[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)


		# Begins Infinite Loop
		while True:

			# Setup Input Variables
			input_one = GPIO.input(BUTTON_ONE)
			input_two = GPIO.input(BUTTON_TWO)
			input_three = GPIO.input(BUTTON_THREE)

			# Determines Sound File Based On GPIO
			if input_one == 0:

				bark.play()
				print("Bark Playing")

				time.sleep(0.5)

			if input_two == 0:

				alien.play()
				print("Alien Playing")

				time.sleep(0.5)

			if input_three == 0:

				bell.play()
				print("Bell Playing")


			else:

				continue

			time.sleep(0.5)



