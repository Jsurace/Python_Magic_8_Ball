"""
Program: magicball.py
Author: Jenna
Date: 4/01/2019

Program which randomly generates a series of string responses in order to respond
to user input as questions. Program uses python GUI. and REQUIRES these files to run breezypythongui.py file
and images.py to utilize Images.
"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage 
from tkinter.font import Font 
import random

class MagicBall(EasyFrame):

	def __init__(self):
	# Creates window and widgets
		EasyFrame.__init__(self, title = "Magic 8 Ball", width = 950, height = 460, background = "black")

		# Image 
		self.image = PhotoImage(file = "8ball2.gif")
		# Text Label for image
		self.imageLabel = self.addLabel(text = "", row = 2, column = 0, sticky = "NSEW",
		background = "DodgerBlue2", foreground = "black") 
		self.imageLabel["image"] = self.image
		

		# User response field
		self.message = self.addLabel(text = "", row = 2, column = 1, sticky = "NSEW")

		# Button
		self.addButton(text = "Ask me anything", row = 3, column = 0, command = self.randomString)

		# Return of responses for output
		self.outputField = self.addTextField(text = "What will be your outcome today?", row = 3, column = 1, state = "readonly")
		
		# Cosmetic styling using color and font selections
		myFont = Font(family = "Verdana", size = 12, slant = "italic")
		thisFont = Font(family = "Arial Bold", size = 10)
		self.message["font"] = myFont
		self.message["foreground"] = "blue"
		self.message["background"] = "black"

		self.outputField["font"] = thisFont
		self.outputField["foreground"] = "blue"
		self.outputField["background"] = "black"

	# Function handeling promper box and event
	def randomString(self):
		# List of string responses
		responses = ("Most Likely Not..", "Absolutely!", "Hmmmm I don't think so..", "Fortune shines upon you my friend",
			"Today is your lucky day!", "Sorry, this is not happening.", "................", "You bet!", "Sorry but NO.",
			"Error Error...Malfunctioning...", "Say what??", "No.. definetly no.", "YES, YES, YES", "Winner Winner Chicken Dinner!",
			"This outlook dosen't seem favorable")

		# Prompter box display - Spits back the user input after user asks their question
		ask = self.prompterBox(title = "Magic 8 Ball Speaks", promptString = "Your Question:")
		
		#self.message = ask.getText(inputText())
		self.message["text"] = "Your reply was: \n" + ask + "?"

		# Event for button giving random responses to user event and displays response to output
		self.outputField.setText(random.choice(responses))

def main():
	MagicBall().mainloop()

main()