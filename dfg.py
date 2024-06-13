# from faker import Faker
from Model.parameter import Parameter
import csv


# Main method
def main():
    # Init
    param = initparameter("./Template/template.json")
    print(param.to_string())

    # Generate
    generate(param, "./output/")


def initparameter(template_path:str) -> Parameter:
    return Parameter(template_path)


def generate(param: Parameter, output:str):

    for file in param.files:
        if file.filetype == 'csv':
            with open(output+file.filename, mode='w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, file.headercolumns)

                # Write the header
                writer.writeheader()

                # Write the data rows
                writer.writerows()
                # Step 1: Prepare your data as a list of dictionaries
            ''' data = [
                    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
                    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
                    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
                ]
                '''


if __name__ == "__main__":
    main()
