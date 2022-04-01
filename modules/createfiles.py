from numpy import number
from word2number import w2n
import datetime
import os

#* create and name files

# TODO find number of files to create
# TODO file types
# TODO (optional parameter) name files



singlefile = ['a', 'one']

filepath = os.path.join('/Users/drewskikatana/titan/test', f'file {datetime.datetime.now()}')


def createfiles(speech):
    speech = speech.split()
    # number_of_files = w2n.word_to_num(speech[1])
    if speech[1] in singlefile:
        open(filepath, 'x')
    else:
        for i in range(int(speech[1])):
            open(f'{filepath}{i}.txt', 'x')
