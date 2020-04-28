import pygame
import time
import RPi.GPIO as GPIO

pygame.init()

# optional sounds 
#bass = pygame.mixer.Sound("/home/pi/final_proj/music_box/samples/bass_dnb_f.wav")
#breaks = pygame.mixer.Sound("/home/pi/final_proj/music_box/samples/loop_amen.wav")
#crow = pygame.mixer.Sound("/home/pi/final_proj/music_box/samples/misc_crow.wav")

#kick = pygame.mixer.Sound("/home/pi/final_proj/music_box/samples/drum_heavy_kick.wav")
#snare = pygame.mixer.Sound("/home/pi/final_proj/music_box/samples/drum_snare_hard.wav")

guitar = pygame.mixer.Sound("/home/pi/final_proj/music_box/samples/guit_e_fifths.wav")
drums = pygame.mixer.Sound("/home/pi/final_proj/music_box/samples/loop_compus.wav")

def button1(pin):
        print("drums")
        drums.play()

def button2(pin):
        print("guitar")
        guitar.play()

#def drum_program(pin):
#       kick.play()
#       print("boom")
#       time.sleep(.3)
#
#       snare.play()
#       print("bap")
#       time.sleep(.6)
#
#       kick.play()
#       print("boom")
#       time.sleep(.15)
#
#       snare.play()
#       print("bap")
#       time.sleep(.3)
#
#       kick.play()
#       print("boom")
#       time.sleep(.15)
#
#       kick.play()
#       print("boom")
#       time.sleep(.3)
#
#       snare.play()
#       print("bap")
#       time.sleep(.6)
#
#       kick.play()
#       print("boom")
#       time.sleep(.15)
#
#       snare.play()
#       print("bap")
#       time.sleep(.3)

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Setup pins and set default state to off
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# GPIO event that detects rising current change (from off to on)
# The button press changes the voltage and triggers a callback function
GPIO.add_event_detect(12, GPIO.RISING,callback=button1)
GPIO.add_event_detect(24, GPIO.RISING,callback=button2)

# Display
print("\n")
print("welcome to the raspberry jam\n")
message = input("press ctrl+c to quit\n")
