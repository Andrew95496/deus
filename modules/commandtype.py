class Command:

# "create 5 files named file1, file2, file3, file4, and file5" as txt

# ? create -> COMMAND
# ? 5 -> number of files to create
# ? [file1, file2, file3, file4, file5] -> Deus names the files
# ? as txt -> file type

    def identification(speech):
        sentance = speech.split()
        return sentance[0]

    def parse(speech):
        speech = speech.split()
        return speech
    
    
