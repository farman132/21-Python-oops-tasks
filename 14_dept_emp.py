class Employee:
    def __init__(self, name):
        self.name = name

class Dept:
    def __init__(self, emp):
        self.emp = emp

e = Employee("Adeel")
d = Dept(e)
print(d.emp.name)
