import RPi.GPIO as GPIO
import pygame
import time

# Variables
RED = 12
BUTTON = 18

# GPIO Setup

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RED, GPIO.OUT)

# Pygame Initialization

pygame.mixer.init()

# Button Press

while True:

	bark = pygame.mixer.Sound("bark.wav")
	input = GPIO.input(BUTTON)

	if input == 0:
		bark.play()
		print("Sound Playing")
	else:
		bark.stop()
		continue

	time.sleep(0.5)

