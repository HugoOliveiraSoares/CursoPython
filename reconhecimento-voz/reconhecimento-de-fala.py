
from speech_recognition import  *

rec = recognizer_instance.Recognizer()

with recognizer_instance.Microphone() as fala:
    frase = rec.listen(fala)

print(rec.recognize_sphinx(frase))
"""
from pocketsphinx import LiveSpeech
for p in LiveSpeech():
    print(p)
"""
