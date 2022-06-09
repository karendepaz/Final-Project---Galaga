from falling_objects import FallingObject

class Rock(FallingObject):
    def __init__(self):
        super(Rock, self).__init__()
        self.appearance = "O"
        self.points = -1