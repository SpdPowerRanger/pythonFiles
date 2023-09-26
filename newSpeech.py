"""
import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)

text = " "

while text not in ('exit', 'Exit','exit.','Exit.'):

	text = input("Input Text : ")

	engine.say(text)

	engine.runAndWait()

	print("Type 'exit' or 'Exit' to quit the program." )

"""

from gtts import gTTS

from playsound import playsound

text_val = """नमस्कार Prakash Yadu Ji."""

language = 'hi'

obj = gTTS(text = text_val, lang = language, slow = False)

obj.save('Bimla.mp3')

playsound("Bimla.mp3")
