from tkinter import *
from button_classes import *

button = Buttons()
frame = Tk()

# Change Note Locations (Button)
ONE = 0
TWO = 1
THREE = 2
FOUR = 3


button.callSound(THREE, "bark.wav")
button.buttonSetup()

testLabel = Label(frame, text = "Yeeee")
testLabel.pack()

frame.mainloop()
