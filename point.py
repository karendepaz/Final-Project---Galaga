class Point:
    """
    The Point class takes care of the objects. A distance from a relative origin (0, 0)
    
    Attributes:
        x
        y
    """

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set_x(self, value):
        self._x = value

    def set_y(self, value):
        self._y = value

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
