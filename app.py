class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, others):
        return self.x == others.x and self.y == others.y


point = Point(1, 2)
others = Point(1, 2)
print(point == others)
