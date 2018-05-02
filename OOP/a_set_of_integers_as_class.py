class intSet(object):

    def __init__(self):
        # create an empty set of integers
        self.vals = []

    def insert(self, e):
        #assumes e is an integer and inserts e into self
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        #assumes e is an integer, returns true if e is false, and false otherwise
        return e in self.vals

    def remove(self, e):
        #assumes e is an integer and removes e from self, Raises ValueError if e is not in self
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + "not found")

    def __str__(self):

        self.vals.sort()
        return "{" + ",".join([str(e) for e in self.vals]) + "}"

s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
s.member(3)
s.member(5)
s.member(6)
print(s)
#s.remove(3)
print(s)
s.remove(3)
print(s)
s.remove(4)
print(s)