class simple:
    def greet(self, name="Student"):
        print("Hello", name)

s = simple()
s.greet("Haresh")
s.greet()

class calculator:
    def add(self, a=0, b=0):
        return a + b

class Student:
    def __init__(self, name, age):   
        print("Student object created")
        self.name = name
        self.age = age

s1 = Student("Mohan", 20)

print(s1.name)
print(s1.age)