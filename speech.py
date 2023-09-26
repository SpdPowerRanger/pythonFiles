"""
from gtts import gTTS

from playsound import playsound

text_val = "सुप्रभात!"

language = "hi"

obj = gTTS(text = text_val, lang = language, slow = False)

obj.save("hindi.mp3")

playsound("hindi.mp3")
"""

"""
from gtts import gTTS

from playsound import playsound

text_val = 

language = "en"

obj = gTTS(text = text_val, lang = language, slow = False)

obj.save('Loneliness.mp3')

playsound("Loneliness.mp3")

"""


import pyttsx3

engine = pyttsx3.init()

text = """ Loneliness:

What is loneliness?

Being alone?

being by yourself?

being away from others?

or not fitting in with yourself?

being uncomfortable around others or one's own self?

a sense of not belonging?

sense of being present but not being included?

a sense, or a feeling of being left behind?

you are the only one left behind while everyone else is in onto something important together.

so, does nothing matters to you without others?

is everything meaningless without others?

does others opinions and attention matter so much?

Focus on yourself.

make yourself a better person.

Improve in silence.

You have a great opportunity.

Nobody's watching.

Whatever you do has no consequence.

Nobody would care if you make a fool out of yourself.

As you are alone.

Be with your own self.

Make your own self sombody that you want to be around.

make yourself into a person that you want to look up to.

You are not alone.

Look around and see what surrounds you.

everything is something that you are not.

without care those things will pass away.

look outside your window.

feel the wind.

feel the aliveness of the world.

see the small creatures moving around.

see the ants.

watch the birds go by.

watch the flowers bloom.

touch the water.

feel its coolness.

the world is around you.

the world is for you.

the world is with you.

You are alone but not lonely.

See past your own self.

Let the world seep into you."""

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

engine.save_to_file(text, 'LonelinessSlow.mp3')

engine.runAndWait()