
'''Practise Method with Default Arguments aka Method Overloading'''

class A:
    def method01(self, i=None):
        if i is None:
            print("Sequence01")
        else:
            print("Sequence02")

def main():
    x = A()
    x.method01()
    x.method01(5)

if __name__ == "__main__":
    main()
