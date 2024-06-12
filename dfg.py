from faker import Faker
from Model.parameter import Parameter


# Main method
def main():
    # Init
    param = initparameter()
    print(param.to_string())

    #Generate
    generate(param)
    #create
    create(param)


def initparameter() -> Parameter:
    return Parameter("./Template/template.json")


def generate(param:Parameter):
    faker = Faker()


# create the files
def create(param):
    pass


if __name__ == "__main__":
    main()
