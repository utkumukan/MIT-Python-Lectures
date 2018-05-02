class coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def distance(self, other):
        x_diff_equ = (self.x - other.x)**2
        y_diff_equ = (self.y - other.y)**2
        return (x_diff_equ + y_diff_equ)**0.5

c = coordinate(3,4)
origin = coordinate(0,0)

print(c.x, origin.x)
print(c.distance(origin))
print(coordinate.distance(c, origin))
print(origin.distance(c))
print(c)
