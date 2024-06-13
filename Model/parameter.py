import json
from typing import List

from Model.fileparam import Fileparam


class Parameter:
    files: List[Fileparam] = []

    def __init__(self, filepath: str):
        # Open the json template
        try:
            with open(filepath, "r") as f:
                data = json.load(f)

                # TODO Loop the data once and get separate content
                for file in data:
                    fileparam = Fileparam(data[file])
                    self.files.append(fileparam)

                '''for item in data["fileDescription"]:
                    if item == 'fileType':
                        self.filetype: str = data["fileDescription"][item]
                    elif item == 'fileName':
                        self.filename: str = data["fileDescription"][item]
                    elif item == 'delimiter':
                        self.delimiter: str = data["fileDescription"][item]
                    elif item == 'hasHeader':
                        self.hasheader: bool = data["fileDescription"][item]
                        if self.hasheader:
                            self.build_header(data)'''

        except FileNotFoundError:
            print(f"Error: The file {filepath} was not found.")
            raise
        except json.JSONDecodeError:
            print(f"Error: The file {filepath} is not a valid JSON file.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def to_string(self) -> str:
        return_str: str = ''
        for file in self.files:
            return_str = return_str+"\n"+file.to_string()
        return return_str
