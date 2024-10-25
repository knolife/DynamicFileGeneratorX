# from faker import Faker
import logging
import random
import pandas as pd

from Model.parameter import Parameter



# Main method
def main():

    # Logging setup 
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    # Init
    param = initparameter("./Template/template.json")
    logging.debug(param.to_string())
    # print(param.to_string())

    # Generate
    generate(param, "./output/")

# Read the template file located in /Template/ folder
def initparameter(template_path: str) -> Parameter:
    return Parameter(template_path)


"""
Core generation method. 
Args :
    param (Object Parameter) : Represent the template config
    output (string) : Folder for the generated file output
"""
def generate(param: Parameter, output: str):
    # loop for each file
    for file in param.files:
        randvalue = ['trfredf', 'edfef', 'gtrgtrgt', '453453']

        # create a tab filled by dict representing a row
        generated_data = []
        # loop for the number of rows wanted
        for count_row in range(file.nbrows):

            # create a dict filled by a generated row below
            generated_data_dict = {}
            for field in file.datafield:
                # TODO implement the generated value stuff
                generated_data_dict[field['name']] = random.choice(randvalue)

            # add the row to the global generated_data tab
            generated_data.append(generated_data_dict)

        df = pd.DataFrame(generated_data, columns=file.headercolumns)

        # Build the CSV with panda
        if file.filetype == 'csv':
            df.to_csv(output + file.filename + '.csv', index=False, sep=file.delimiter, encoding='utf-8')


if __name__ == "__main__":
    main()
