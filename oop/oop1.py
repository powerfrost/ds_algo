
'''
This is a
mult-line docstring
'''

class Point:
    '''This is a class that defines
    a point in 3 dimensional space'''


    def __init__(self, x, y, z):
        '''This is the docstring of init'''
        self.assign(x, y, z)

    def assign(self, x, y, z):
        '''This is a docstring assign!!'''
        self.x = x
        self.y = y
        self.z = z

    def printPoint(self):
        print(self.x, self.y, self.z)



p1 = Point(1,2,3)

print(p1.__doc__)
