import datetime
import os
import itertools
from platform import python_branch

from word2number import w2n


#* create and name files

#* FILE TYPES
# txt
# programming
# xlsx
# pdf
# doc/ docx
# 

#! TODO find number of files to create
# TODO file types
#! TODO (optional parameter) name files
#! TODO Having problems with the mismatching files numbers

# EXAMPLE COMMAND:

#     "create 5 files named file1, file2, file3, file4, and file5" as txt

# ? create -> COMMAND
# ? 5 -> number of files to create
# ? [file1, file2, file3, file4, file5] -> Deus names the files
# ? as txt -> file type

class Files:

    def generate(speech):
        speech = speech.split()
        singlefile = ['a', 'one']
    
        filepath = os.path.join('/Users/drewskikatana/deus/test', f'file {datetime.datetime.now()}')
        
        # document type
        if 'as' in speech:
            doctype = speech[-1].lower()
            index = speech.index('as')
            speech = speech[:index]
        else:
            doctype = 'txt'

        number_of_files = w2n.word_to_num(speech[1])
        if 'named' in speech or 'name' in speech:
            file_names = speech[4:]

            if 'and' in file_names:
                while 'and' in file_names:
                    file_names.remove('and')


            if len(file_names) == int(number_of_files):
                for file_name in file_names:
                    open(f'/Users/drewskikatana/deus/test/{file_name}.{doctype}', 'x')


            elif len(file_names) < number_of_files: #! not enough file names
                print('not enough file names given. ')
                #* When the user asks for more files than what is named the system 
                #* will automatically create the extra timestamped files needed
                # * and give a warning to he user
                number_of_files = number_of_files - len(file_names)
                for file_name in file_names:
                    open(f'/Users/drewskikatana/deus/test/{file_name}.{doctype}', 'x')
                for i in itertools.count(start=0, step=1): 
                    if i < number_of_files:
                        open(f'{filepath}_{i}.{doctype}', 'x')
                    else:
                        break
            elif len(file_names) > number_of_files: #! too many file names
                
                #* When the user names more files than what was suggested
                #* the system will ctreate those named files with a warning
                extra_files = len(file_names) - number_of_files - 1
                print(f'CAUTION: more files named than files number asked for.\n\textra files created: {file_names[extra_files:]}.{doctype} ')

        elif speech[1] in singlefile:
            open(filepath, 'x')
            
        else:
            try:
                for i in itertools.count(start=0, step=1): 
                    if i < int(speech[1]):
                        open(f'{filepath}_{i}.{doctype}', 'x')
                    else:
                        break
            except ValueError:
                for i in itertools.count(start=0, step=1): 
                    if i < number_of_files:
                        open(f'{filepath}_{i}.{doctype}', 'x')
                    else:
                        break