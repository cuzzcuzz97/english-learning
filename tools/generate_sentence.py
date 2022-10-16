from wonderwords import RandomWord
from wonderwords import RandomSentence
from googletrans import Translator, constants
import time

translator = Translator()
r = RandomWord()
s = RandomSentence()
# generate a random word
while True:
	w = r.word()
	translation = translator.translate(w, dest="vi",src="en")
	print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
	time.sleep(.5)
