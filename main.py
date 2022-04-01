import sys
from modules.commandtype import command
from modules.createfiles import createfiles
import speech_recognition as sr

# TODO parse through the command




# print(sys.argv[1])

_TIMEOUT = 7

if sys.argv[1] == 'listen':
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Titan is listening...')
        audio = voice_recognizer.listen(source, _TIMEOUT)
        print('I got it!')

    recognized_speech = voice_recognizer.recognize_google(audio)

    print(f'What was heard: {recognized_speech}')

if command(recognized_speech) == 'create':
    createfiles(recognized_speech)

