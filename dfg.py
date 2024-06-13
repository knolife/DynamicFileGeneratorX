# from faker import Faker
import random

from Model.parameter import Parameter
import pandas as pd


# Main method
def main():
    # Init
    param = initparameter("./Template/template.json")
    # print(param.to_string())

    # Generate
    generate(param, "./output/")


def initparameter(template_path: str) -> Parameter:
    return Parameter(template_path)


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
