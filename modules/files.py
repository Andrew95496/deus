class Files:

# PARSED.DICT
#* {'number of files': 1, 'isnamed': True, 'doctype': 'txt', 'filenames': ['Andrew'], 'cautions': 'unnamed files'}

    def generate(self, parsed_dict):
        for file in parsed_dict['filenames']:
            with open(f'/Users/drewskikatana/deus/test/{file}.{parsed_dict["doctype"]}', 'w') as new_file:
                print(f'caution: {parsed_dict["cautions"]} ')




if __name__ == "__main__":
    file = Files()
    file.generate({'number of files': 1, 'isnamed': True, 'doctype': 'txt', 'filenames': ['Andrew'], 'cautions': 'unnamed files'})