
'''Practise multilevel inheritance'''

class Person:

    def assign(self, name, age):
        'Basic assignment of name and age'
        self.name = name
        self.age = age

    def speak(self):
        return(self.name + ", " + str(self.age))

class Employee(Person):

    def assignemp(self, idno):
        self.id = idno

class Programmer(Employee):

    def assignprog(self, lang):
        self.lang = lang

def main():
    Obj1 = Programmer()
    Obj1.assign('xavier', 32)
    Obj1.assignemp(300)
    Obj1.assignprog('Python')
    print(Obj1.name, Obj1.age, Obj1.id, Obj1.lang)

if __name__ == "__main__":
    main()
