__author__ = 'JP'


class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def diff(self, other):
        if not isinstance(other, Point):
            raise TypeError
        x = abs(self.X-other.X)
        y = abs(self.Y-other.Y)
        if y == 3:
            y = 1
        return x+y


