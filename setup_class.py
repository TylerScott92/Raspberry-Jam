import RPi.GPIO as GPIO	
import pygame
import time

class RJam:

	# Global list to hold all sound files
	notes = []
	note_names = []
	current_note = " "
	button_list = []
	loopState = False

	def __init__(self):

		print("Button Constructor")

	def initialSetup(self):

		# Assign initial notes to sound files
		C = "bark.wav"
		D = "alien.wav"
		E = "bell.wav"
		F = "bark.wav"
		G = "alien.wav"
		A = "bark.wav"
		B = "bell.wav"

		# Store file names a string in a list
		global note_names
		note_names = [C, D, E, F, G, A, B]

		# Initialie pygame mixer
		pygame.mixer.init()

		# Adding the files to pygame
		first = pygame.mixer.Sound(C)
		second = pygame.mixer.Sound(D)
		third = pygame.mixer.Sound(E)
		fourth = pygame.mixer.Sound(F)
		fifth = pygame.mixer.Sound(G)
		sixth = pygame.mixer.Sound(A)
		seventh = pygame.mixer.Sound(B)

		# Store pygame sounds in global list
		global notes
		notes = [first, second, third, fourth, fifth, sixth, seventh]

	def changeSound(self, index, file):

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

		# Update list based on file and index number
		if index == ONE:
			first = pygame.mixer.Sound(file)
			notes[0] = first

			##### Change note names in this satement too #####


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
		global button_list
		button_list = [BUTTON_ONE, BUTTON_TWO, BUTTON_THREE, BUTTON_FOUR, BUTTON_FIVE, BUTTON_SIX, BUTTON_SEVEN]

		##### Put this up in the change file function #####
		global note_names
		name_one = note_names[0]
		name_two = note_names[1]
		name_three = note_names[2]
		name_four = note_names[3]
		name_five = note_names[4]
		name_six = note_names[5]
		name_seven = note_names[6]

		# GPIO Setup
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		for i in range (7):
			GPIO.setup(button_list[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

	def loopStatus(self):

		# Begins Infinite Loop
		while loopState == True:

			# Store current note as string
			global current_note

			# List of gpio pins
			global button_list

			# Opens the currently set notes in list
			global notes
			note_one = notes[0]
			note_two = notes[1]
			note_three = notes[2]
			note_four = notes[3]
			note_five = notes[4]
			note_six = notes[5]
			note_seven = notes[6]

			# Opens the currently set note names
			global note_names
			name_one = note_names[0]
			name_two = note_names[1]
			name_three = note_names[2]
			name_four = note_names[3]
			name_five = note_names[4]
			name_six = note_names[5]
			name_seve = note_names[6]

			# Setup Input Variables
			input_one = GPIO.input(button_list[0])
			input_two = GPIO.input(button_list[1])
			input_three = GPIO.input(button_list[2])
			input_four = GPIO.input(button_list[3])
			input_five = GPIO.input(button_list[4])
			input_six = GPIO.input(button_list[5])
			input_seven = GPIO.input(button_list[6])

			# Determines Sound File Based On GPIO
			if input_one == 0:

				note_one.play()
				print("Bark Playing")
				current_note = name_one
				print(current_note)

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

				time.sleep(0.5)

			else:

				continue

			time.sleep(0.5)


	def beginLoop(self):
		global loopState
		loopState = True
		self.loopStatus()

	def breakLoop(self):

		global loopState
		loopState = False
		self.loopStatus()

#	def getCurrentNote(self):

#		global current_note
#		note = current_note
#		return note



