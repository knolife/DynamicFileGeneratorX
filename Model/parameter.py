import json

class Parameter():

    def __init__(self, filepath:str):
        # Open the json template
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                for item in data["fileDescription"]:
                    if (item=='fileType'):
                        self.filetype = data["fileDescription"][item]
                    elif (item=='fileName'):
                        self.filename = data["fileDescription"][item]
                    elif (item=='delimiter'):
                        self.delimiter = data["fileDescription"][item]

        except FileNotFoundError:
            print(f"Error: The file {filepath} was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file {filepath} is not a valid JSON file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def to_string(self):
            return f"Hello, my name is {self.filename} and I am {self.filetype} with a delimiter as {self.delimiter}"
