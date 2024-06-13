# from faker import Faker
from Model.parameter import Parameter


# Main method
def main():
    # Init
    param = initparameter()
    print(param.to_string())

    # Generate
    generate(param)


def initparameter() -> Parameter:
    return Parameter("./Template/template.json")


def generate(param: Parameter):
    if param.hasheader:
        pass
    # faker = Faker()


if __name__ == "__main__":
    main()
