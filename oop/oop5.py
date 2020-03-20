

'''Practising class inheritance'''

class Person:
    var4 = 7

    def method1(self, a, b, c):
        self.var1 = a
        self.var2 = b
        self.var3 = c

class Employee(Person):
    var4 = 9
    pass


def main():
    obj1 = Person()
    obj2 = Employee()

    obj1.method1(1,2,3)
    print(obj1.var1, obj1.var2, obj1.var3, obj1.var4)

    obj2.method1(4,5,6)
    print(obj2.var1, obj2.var2, obj2.var3, obj2.var4)



if __name__ == "__main__":
    main()
