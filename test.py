import math
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Shape x = {} y = {}".format(self.x, self.y)

x = Shape(5, 5)
print(x)
# <__main__.Shape object at 0x00B2FF30>
# Shape x = 5 y = 5
class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r
    def __repr__(self):
        return "Circle x = {} y = {} r = {}".format(self.x, self.y, self.r)
    def area(self):
        return math.pi*self.r**2
    def circumference(self):
        return math.pi*2*self.r
y = Circle(5, 5)

