import datetime
import itertools

from word2number import w2n

from modules.memory import Memory


class Parser:

    def __init__(self, speech):
        self.speech = speech.split()
        self.parsed_dict = {}

# "create 5 files named file1 file2 file3 file4 and file5 as txt"

# ? create -> COMMAND
# ? 5 -> number of files to create
# ? [file1, file2, file3, file4, file5] -> Deus names the files
# ? as txt -> file type

    def parsed(self):  

        # remove 'and'
        if 'and' in self.speech:
            while 'and' in self.speech:
                self.speech.remove('and')      
        

        # file number
        try:
            self.parsed_dict["number of files"] = int(self.speech[1])
        except ValueError:
            self.parsed_dict["number of files"] = w2n.word_to_num(self.speech[1])

        # checking if user wants files named
        if 'named' in self.speech:
            self.parsed_dict['isnamed'] = True
        else:
            self.parsed_dict["isnamed"] = False

        # setting the document type
        if 'as' in self.speech:
            defaultdoctype = False
            self.parsed_dict["doctype"] = self.speech[-1]
        else:
            defaultdoctype = True
            self.parsed_dict["doctype"] = 'txt'

        isnamed = self.parsed_dict['isnamed']
        self.parsed_dict["filenames"] = []
        
        # checks the names and docoument types of the files
        if isnamed and defaultdoctype:
            index1 = self.speech.index('named') + 1
            self.parsed_dict["filenames"] = self.speech[index1:]
        elif isnamed and not defaultdoctype:
            index1 = self.speech.index('named') + 1
            index2 = self.speech.index('as')
            self.parsed_dict["filenames"] = self.speech[index1: index2]
        if not isnamed and defaultdoctype:
            for i in itertools.count(start=0, step=1):
                if i < self.parsed_dict['number of files']:
                    self.parsed_dict["filenames"].append(f'file_{datetime.datetime.now()}_{i+1}')
                else:
                    break
        elif not isnamed and not defaultdoctype:
            for i in itertools.count(start=0, step=1):
                if i < self.parsed_dict['number of files']:
                    self.parsed_dict["filenames"].append(f'file_{datetime.datetime.now()}_{i+1}')
                else:
                    break

        # checking to see if the number of files requested and the number of filenames given match
        if isnamed:
            if self.parsed_dict['number of files'] > len(self.parsed_dict['filenames']):
                self.parsed_dict['cautions'] = 'unnamed files'
            elif self.parsed_dict['number of files'] < len(self.parsed_dict['filenames']):
                self.parsed_dict['cautions'] = 'too many filenames'
            else:
                self.parsed_dict['cautions'] = 0

        # if filenames and files requested dont match add extras to the list
            if self.parsed_dict['cautions'] == 'unnamed files':
                extra_files = self.parsed_dict['number of files'] - len(self.parsed_dict['filenames'])
                for i in itertools.count(start=0, step=1):
                    if i < extra_files:
                        self.parsed_dict["filenames"].append(f'file_{datetime.datetime.now()}_{i+1}')
                    else:
                        break
            elif self.parsed_dict['cautions'] == 'too many filenames':
                print(f"You requested {self.parsed_dict['number of files']} file(s), {len(self.parsed_dict['filenames'])} filenames given")

        memory = Memory()
        memory.INSERT(self.parsed_dict)
        return self.parsed_dict




if __name__ == "__main__":
    for _ in range(1000):
        test1 = Parser("create 5 files named  file1 and file2 and file3 and file4 and file5 as python")
        test2 = Parser("create 5 files named  file1 file2 file3 file4 and file5")
        test3 = Parser("create 3 files")
        test4 = Parser("create 3 files as python")
        test5 = Parser("create 16 files named  file1 file2 file3 file4 and file5 as python")
        test6 = Parser("create 4 files named  file1 file2 file3 file4 and file5 as python")


        print(f'test1: {test1.parsed()}')
        print(f'test2: {test2.parsed()}')
        print(f'test3: {test3.parsed()}')
        print(f'test4: {test4.parsed()}')
        print(f'test5: {test5.parsed()}')
        print(f'test6: {test6.parsed()}')

        print(f'\n\n\n{test1.__dict__}\n\n\n')
