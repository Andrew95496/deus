import sys
from modules.commandtype import command
from modules.createfiles import createfiles
import speech_recognition as sr

# TODO parse through the command

_TIMEOUT = 7


if len(sys.argv) <= 1:
    print('''Welcome to Titan v0.0.1
    
\tfor help type: 'titan help'
    ''')


# print(sys.argv[1])


elif sys.argv[1] == 'listen':
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Titan is listening...')
        audio = voice_recognizer.listen(source, _TIMEOUT)
        print('I got it!')

    recognized_speech = voice_recognizer.recognize_google(audio)

    print(f'What was heard: {recognized_speech}')

    if command(recognized_speech) == 'create':
        createfiles(recognized_speech)

