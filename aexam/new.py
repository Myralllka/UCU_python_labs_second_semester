class A:
    def one(self):
        return self.two()

    def two(self):
        return 'A'

class B(A):
    def two(self):
        return 'B'

a = A()
b = B()
print(a.two(), b.one())