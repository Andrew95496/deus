import sys
import os
from modules.parse import Parser
import speech_recognition as sr


from modules.commandtype import Command
from modules.files import Files
from modules.web import Web
from config import __version__, _TIMEOUT
from user_configs.user_configs import SAVED_COMMANDS

# TODO parse through the command
# TODO add a save command


if len(sys.argv) <= 1:
    print(f'''\nWelcome to DEUS "{__version__}"

\tfor help type: 'deus help'
    ''')


# * LISTEN COMMAND
if sys.argv[1] == 'listen':
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Titan is listening...')
        audio = voice_recognizer.listen(source, _TIMEOUT)
        print('I got it!')

    recognized_speech = voice_recognizer.recognize_google(audio)

    print(f'What was heard: {recognized_speech}')


    if Command.identification(recognized_speech) in SAVED_COMMANDS:
        pass
# titan is listening for the 'CREATE' command
    elif Command.identification(recognized_speech) == 'create':
        speech = Parser(recognized_speech)
        Files.generate(speech.file_parse())

    elif Command.identification(recognized_speech) == 'build':
        speech = Parser(recognized_speech)
        Web.generate(speech.web_parse())


# * MEMORY COMMAND
if sys.argv[1] == 'mem':
    os.system('cat .memory')


if __name__ == "__main__":
    pass
