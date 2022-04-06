import datetime
import os
import math

from pandas import ExcelFile


class Memory:

    def __init__(self):
        self.database = {}

    def __convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f'Memory Size: {s} {size_name[i]}'

    def INSERT(self, data):
        self.database[f'{datetime.datetime.now()}'] = data
        with open('.memory.txt', 'a') as memory:
            memory.write(f'{self.database}\n')

        bytes = os.path.getsize('/Users/drewskikatana/deus/.memory.txt')

        return self.__convert_size(bytes)




if __name__ == "__main__":

    m = Memory()

    print(m.INSERT('1'))

