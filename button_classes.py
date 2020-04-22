import RPi.GPIO as GPIO
import pygame
import time

class Buttons:

	# Global list to hold all sound files
	notes = []

	def __init__(self):

		print("Button Constructor")

	def callSound(self, index, file):

		# Mixer initialization
		pygame.mixer.init()

		# Assign names to variables
		C = "bark.wav"
		D = "alien.wav"
		E = "bell.wav"
		F = "bark.wav" 
		G = "alien.wav"
		A = "bell.wav"
		B = "bark.wav"

		# Assign file to mixer 
		first = pygame.mixer.Sound(C)
		second = pygame.mixer.Sound(D)
		third = pygame.mixer.Sound(E)
		fourth = pygame.mixer.Sound(F)
		fifth = pygame.mixer.Sound(G)
		sixth = pygame.mixer.Sound(A)
		seventh = pygame.mixer.Sound(B)

		# Index locations
		ONE = 0
		TWO = 1
		THREE = 2
		FOUR = 3
		FIVE = 4
		SIX = 5
		SEVEN = 6

		# Call notes list and initialize starting list
		global notes
		notes = [first, second, third, fourth, fifth, sixth, seventh]

		# Update list based on file and index number
		if index == ONE:
			first = pygame.mixer.Sound(file)
			notes[0] = first


		if index == TWO:
			second = pygame.mixer.Sound(file)
			notes[1] = second

		if index == THREE:
			third = pygame.mixer.Sound(file)
			notes[2] = third

		if index == FOUR:
			fourth = pygame.mixer.Sound(file)
			notes[3] = fourth

		if index == FIVE:
			fifth = pygame.mixer.Sound(file)
			notes[4] = fifth

		if index == SIX:
			sixth = pygame.mixer.Sound(file)
			notes[5] = sixth

		if index == SEVEN:
			notes[6] = seventh

	def buttonSetup(self):

		# Variables
		BUTTON_ONE = 12
		BUTTON_TWO = 16
		BUTTON_THREE = 18
		BUTTON_FOUR = 22
		BUTTON_FIVE = 11
		BUTTON_SIX = 13
		BUTTON_SEVEN = 15

		# Put GPIO pins in list
		button_list = [BUTTON_ONE, BUTTON_TWO, BUTTON_THREE, BUTTON_FOUR, BUTTON_FIVE, BUTTON_SIX, BUTTON_SEVEN]

		# Access notes from global variable
		global notes
		note_one = notes[0]
		note_two = notes[1]
		note_three = notes[2]
		note_four = notes[3]
		note_five = notes[4]
		note_six = notes[5]
		note_seven = notes[6]

		# GPIO Setup
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		for i in range (7):
			GPIO.setup(button_list[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)


		# Begins Infinite Loop
		while True:

			# Setup Input Variables
			input_one = GPIO.input(BUTTON_ONE)
			input_two = GPIO.input(BUTTON_TWO)
			input_three = GPIO.input(BUTTON_THREE)
			input_four = GPIO.input(BUTTON_FOUR)
			input_five = GPIO.input(BUTTON_FIVE)
			input_six = GPIO.input(BUTTON_SIX)
			input_seven = GPIO.input(BUTTON_SEVEN)

			# Determines Sound File Based On GPIO
			if input_one == 0:

				note_one.play()
				print("Bark Playing")

				time.sleep(0.5)

			if input_two == 0:

				note_two.play()
				print("Alien Playing")

				time.sleep(0.5)

			if input_three == 0:

				note_three.play()
				print("Bell Playing")

				time.sleep(0.5)

			if input_four == 0:

				note_four.play()
				print("New Working")

				time.sleep(0.5)

			if input_five == 0:

				note_five.play()
				print("Five")

				time.sleep(0.5)

			if input_six == 0:

				note_six.play()
				print("Six")

				time.sleep(0.5)

			if input_seven == 0:

				note_seven.play()
				print("Seven")



			else:

				continue

			time.sleep(0.5)



