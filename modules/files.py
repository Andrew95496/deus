import datetime


class Files:

# PARSED.DICT
#* {'number of files': 1, 'isnamed': True, 'doctype': 'txt', 'filenames': ['Andrew'], 'cautions': 'unnamed files'}

    def generate(self, parsed_dict):
        for file in parsed_dict['filenames']:
            with open(f'/Users/drewskikatana/deus/test/{file}.{parsed_dict["doctype"]}', 'w'):
                if parsed_dict['cautions'] != 0:
                    print(f'Files created with cautions!\n\tcaution: {parsed_dict["cautions"]} ')
                else:
                    print('SUCCESS!')




if __name__ == "__main__":
    file = Files()
    file.generate({'number of files': 1, 'isnamed': True, 'doctype': 'sh', 'filenames': [f'{datetime.datetime.now()}'], 'cautions': 'unnamed files'})