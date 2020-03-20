

'''Practising class inheritance +'''

class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return self.first + " " + self.last + ", " + str(self.age)

class Employee(Person):
    def __init__(self, first, last, age, sal):
        super().__init__(first, last, age)
        self.sal = sal

    def __str__(self):
        return super().__str__() +  ", " + str(self.sal)


def main():
    x = Person('Xavier', 'Chia', 32)
    print(x)

    y = Employee('George', 'Boon', 18, 5500)
    print(y)


if __name__ == "__main__":
    main()
