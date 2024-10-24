from typing import List

class Fileparam:
    filetype: str
    filename: str
    delimiter: str
    hasheader: bool = True
    nbrows: int

    header: str = ''
    headercolumns = []
    datafield = [] 

    def __init__(self, file: str):

        self.headercolumns = []
        self.datafield = file['columns']

        for item in file:
            if item == 'fileType':
                self.filetype: str = file[item]
            elif item == 'fileName':
                self.filename: str = file[item]
            elif item == 'nbRows':
                self.nbrows: int = file[item]
            elif item == 'delimiter':
                self.delimiter: str = file[item]
            elif item == 'hasHeader':
                self.hasheader: bool = file[item]

        if self.hasheader:
            self.build_header(file['columns'])


    def build_header(self, columns):
        for column in columns:
            if column['name']:
                # Build first line header as string
                self.header = self.header + column['name'] + self.delimiter
                # Tab of each column
                self.headercolumns.append(column['name'])

    def to_string(self):
        return (f"Hello, my name is {self.filename} and I am {self.filetype} with a delimiter as {self.delimiter}"
                + "\nHeader : " + self.header)
