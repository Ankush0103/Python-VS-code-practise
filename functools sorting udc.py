import functools
from functools import total_ordering

@total_ordering
class UDC:
    print("Inside class")

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, obj):
        return ((self.b) < (obj.b))

    def __gt__(self, obj):
        return ((self.b) > (obj.b))

    def __le__(self, obj):
        return ((self.b) <= (obj.b))

    def __ge__(self, obj):
        return ((self.b) >= (obj.b))

    def __eq__(self, obj):
        return (self.b == obj.b)

    def __repr__(self):
        return str((self.a, self.b))

# list of objects
udc = [UDC("geeks", 1), UDC("computer", 3), UDC("for", 2), UDC("geeks", 4), UDC("science", 3)]

print(udc) # Before sorting

print(sorted(udc)) # After sorting on basis of variables stored in b
