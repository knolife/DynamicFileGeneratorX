import json
from typing import List

from Model.fileparam import Fileparam


class Parameter:
    files: List[Fileparam] = []

    def __init__(self, filepath: str):
        # Open the json template and create the list of fileparam
        try:
            with open(filepath, "r") as f:
                data = json.load(f)

                for file in data:
                    fileparam = Fileparam(data[file])
                    self.files.append(fileparam)

        except FileNotFoundError:
            print(f"Error: The file {filepath} was not found.")
            raise
        except json.JSONDecodeError:
            print(f"Error: The file {filepath} is not a valid JSON file.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    # Detail the content of each file in the template
    def to_string(self) -> str:
        return_str: str = ''
        for file in self.files:
            return_str = return_str+"\n"+file.to_string()
        return return_str
