class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}  Marks: {self.marks}")

# Object banaya
s1 = Student("Farman", 98)
s1.display()
