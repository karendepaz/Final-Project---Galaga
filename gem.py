from falling_objects import FallingObject

class Gem(FallingObject):
    def __init__(self):
        super(Gem, self).__init__()
        self.appearance = "*"
        self.points = 1
