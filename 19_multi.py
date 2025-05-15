class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, val):
        return val * self.factor

m = Multiplier(5)
print(callable(m))
print(m(10))
