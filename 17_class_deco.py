def add_greet(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greet
class Person:
    pass

p = Person()
print(p.greet())
