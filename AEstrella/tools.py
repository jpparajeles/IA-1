__author__ = 'JP'


class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def diff(self, other):
        if not isinstance(other, Point):
            raise TypeError
        x = abs(self.X-other.X)
        if x == 3:
            x = 1
        y = abs(self.Y-other.Y)
        return x+y


