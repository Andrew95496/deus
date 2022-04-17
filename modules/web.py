import imp
from datetime import datetime
import os


class Web:
    

    def generate(self):
        dir_name = 'p'
        os.mkdir(f'/Users/drewskikatana/deus/test/{dir_name}')
        os.system(f'touch /Users/drewskikatana/deus/test/{dir_name}/index.html')
        os.system(f'touch /Users/drewskikatana/deus/test/{dir_name}/styles.css')
        os.system(f'touch /Users/drewskikatana/deus/test/{dir_name}/app.js')
        



if __name__ == "__main__":
    web = Web()

    web.generate()