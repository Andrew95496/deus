import datetime
import os
import math

#TODO encrypt memory only decryted by private key


class Memory:

    def __init__(self):
        self.database = {}

    def __encrypt(self, data):
        ascii_data = []
        for char in data:
            ascii = ord(char) + 7
            ascii_data.append(str(ascii))
        return ' '.join(ascii_data)


    def decrypt(self, data):
        pass

    # converting the size of the file to the size name
    # hidden method
    def __convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f'Memory Size: {s} {size_name[i]}'

    # insert the data into local memory
    def INSERT(self, data):
        with open('.memory', 'a') as memory:
            self.database[f'{datetime.datetime.now()}'] = data
            ascii_string = f'{self.database}'
            print(ascii_string)
            memory.write(f'{self.__encrypt(ascii_string)}\n')

        

        bytes = os.path.getsize('/Users/drewskikatana/deus/.memory')

        return self.__convert_size(bytes)




if __name__ == "__main__":

    m = Memory()

    for i in range(5000):
        data = str(os.urandom(5))
        i = Memory()
        print(i.INSERT(data))

