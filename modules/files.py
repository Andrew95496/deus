from numpy import number
from word2number import w2n
import datetime
import os

#* create and name files

# TODO find number of files to create
# TODO file types
# TODO (optional parameter) name files

class Files:

    def generate(speech):
        singlefile = ['a', 'one']
    
        filepath = os.path.join('/Users/drewskikatana/titan/test', f'file {datetime.datetime.now()}')
        speech = speech.split()
        number_of_files = w2n.word_to_num(speech[1])
        if 'named' in speech:
            file_names = speech[4:]
            if 'and' in file_names:
                file_names.remove('and')
            for files_name in file_names:
                open(f'/Users/drewskikatana/titan/test/{files_name}', 'x')
        elif speech[1] in singlefile:
            open(filepath, 'x')
        else:
            try:
                for i in range(int(speech[1])):
                    open(f'{filepath}{i}.txt', 'x')
            except ValueError:
                for i in range(number_of_files):
                    open(f'{filepath}{i}.txt', 'x')