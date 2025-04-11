import math


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def update_vector(self, x, y):
        self.x  = x
        self.y  = y
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y


    def __iadd__(self, other):
        if isinstance(other, Vector2):
            self.update_vector(self.get_x() + other.get_x(),
                               self.get_y() + other.get_y())
        else:
            assert "Vector2: You are trying to add a non Vector2 type"
        return self

    def __imul__(self, other):
        if isinstance(other, Vector2):
            self.update_vector(self.get_x() * other.get_x(),
                               self.get_y() * other.get_y())
        else:
            assert "Vector2: You are trying to multiplicate a non Vector2 type"

        return self

    def unpack(self):
        return self.get_x(), self.get_y()

def distance(a: Vector2, b: Vector2):
    return math.hypot(b.x-a.x, b.y-a.y)
