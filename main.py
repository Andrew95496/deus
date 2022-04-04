import sys
from modules.parse import Parser
import speech_recognition as sr


from modules.commandtype import Command
from modules.files import Files
from config import __version__, _TIMEOUT

# TODO parse through the command
# TODO add a save command



if len(sys.argv) <= 1:
    print(f'''\nWelcome to DEUS "{__version__}"

\tfor help type: 'deus help'
    ''')


elif sys.argv[1] == 'listen':
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Titan is listening...')
        audio = voice_recognizer.listen(source, _TIMEOUT)
        print('I got it!')

    recognized_speech = voice_recognizer.recognize_google(audio)

    print(f'What was heard: {recognized_speech}')

# titan is listening for the 'CREATE' command
    if Command.identification(recognized_speech) == 'create':
        speech = Parser(recognized_speech)
        Files.generate(speech.parsed())

