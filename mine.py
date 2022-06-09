from falling_objects import FallingObject

class Mine(FallingObject):
    def __init__(self):
        super(Mine, self).__init__()
        self.appearance = "X"
        self.points = -20