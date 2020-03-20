'''This is oop2'''

class Class01:
    '''This is the doc for Class01'''
    def __init__(self):
        '''This is the doc for Class01 __init__'''
        print("Created an object for the Class01")

class Class02:

    def __init__(self):
        print("Created an object for the Class02")

def main():
    '''This is the main docstring for oop2 module'''
    O1 = Class01()
    O2 = Class02()


if __name__ == "__main__":
    print("The module oop2 is being run directly")
else:
    print("The module oop2 is being run as an import")
