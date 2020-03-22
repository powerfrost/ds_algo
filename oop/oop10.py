
'''Practise hybrid inheritance and diamond of death'''

class A:
    def m(self):
        print("This is m() from class A...")

class B(A):
    def m(self):
        print("This is m() from class B...")
        super().m()


class C(A):
    def m(self):
        print("This is m() from class C...")
        super().m()


class D(B, C):
    def m(self):
        print("This is m() from class D...")
        super().m()


def main():
    Obj1 = D()
    print(D.__mro__)
    print(Obj1.m())

if __name__ == "__main__":
    main()
