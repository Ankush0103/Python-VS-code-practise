class UDC:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return str((self.a, self.b))

# List of Objects
udc = [UDC("geeks", 1), UDC("computer", 3), UDC("for", 2), UDC("geeks", 4), UDC("science", 3)]

# sorting objects based on value stored at variable b
print(sorted(udc, key=lambda x: x.b))