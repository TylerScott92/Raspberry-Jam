from guizero import App, PushButton, Slider, TextBox, Text
from button_classes import *

app = App(title = "GUI test")
jam = RJam()

ONE= 0
TWO = 1
THREE = 2
FOUR = 3

jam.initialSetup()
jam.buttonSetup()

# Works only if before buttonSetup()
#jam.changeSound(TWO, "bell.wav")

def update_text():
	label.value = name.value

def startLoop():
	start_button.disable()
	stop_button.enable()
	jam.beginLoop()

def endLoop():
	start_button.enable()
	stop_button.disable()
	jam.breakLoop()

#current_note = button.getCurrentNote()
label = Text(app, text = "YO")
name = TextBox(app)
push_button = PushButton(app, command = update_text)
start_button = PushButton(app, command = startLoop, text = "start")
stop_button = PushButton(app, command = endLoop, text = "end")


app.display()


