class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __iadd__(self, other):
        self.height += other
        return self
    def __isub__(self, other):
        self.height -= other
        return self