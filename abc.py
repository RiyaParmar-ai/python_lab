from abc import ABC, abstractmethod

#1
"""class Vehicle(ABC) :
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle) :
    def start(self):
        print("Car starts with key")

c = Car()    # object created
c.start()    # method called"""

#2
"""class Animal(ABC) :
    @abstractmethod
    def sound(self):
        pass

class Cat(Animal) :
    def sound(self):
        print("Cat Meows")

c = Cat()
c.sound() """

#3
"""class Vehicle(ABC) :
     @abstractmethod
     def start(self):
        pass

class Bike(Vehicle) :
    def start(self):
        print("Bike starts with self-start")

b = Bike()
b.start()"""  

#4
"""class Shape(ABC) :
     @abstractmethod
     def area(self):
        pass

class Circle(Shape) :
    def area(self):
        print("Area of Circle = pi * r * r")

ci = Circle()
ci.area()"""        

#5
"""class Appliance(ABC) :
     @abstractmethod
     def switch_on(self):
        pass

class Fan(Appliance) :
    def switch_on(self):
        print("Fan is switched on")

f = Fan()
f.switch_on() """       

#6
"""class Bird(ABC) :
     @abstractmethod
     def fly(self):
        pass

class Sparrow(Bird) :
    def fly(self):
        print("Sparrow flies high")

sp = Sparrow()
sp.fly()        

#7
class Employee(ABC) :
     @abstractmethod
     def work(self):
        pass

class Teacher(Employee) :
    def work(self):
        print("Teacher teaches students")

t = Teacher()
t.work()        

#8
class Payment(ABC) :
     @abstractmethod
     def pay(self):
        pass

class UPI(Payment) :
    def pay(self):
        print("Payment done using UPI")

u = UPI()
u.pay() 

#9
class Instrument(ABC) :
     @abstractmethod
     def play(self):
        pass

class Guitar(Instrument) :
    def play(self):
        print("Guitar is playing")

g = Guitar()
g.play() 

#10
class Phone(ABC) :
     @abstractmethod
     def call(self):
        pass

class Smartphone(Phone) :
    def call(self):
        print("Calling from smartphone")

p = Smartphone()
p.call() 

#11
class Food(ABC) :
     @abstractmethod
     def taste(self):
        pass

class Pizza(Food) :
    def taste(self):
        print("Pizza tastes delicious")

pi = Pizza()
pi.taste()

#12
class Fruit(ABC) :
     @abstractmethod
     def taste(self):
        pass

class Mango(Fruit) :
    def taste(self):
        print("Mango tastes sweet and sour at the same time")

m = Mango()
m.taste() 

#13
class Student(ABC) :
     @abstractmethod
     def study(self):
        pass

class CollegeStudent(Student) :
    def study(self):
        print("College student studies daily")

cs = CollegeStudent()
cs.study() 

#14
class Machine(ABC) :
     @abstractmethod
     def work(self):
        pass

class Computer(Machine) :
    def work(self):
        print("Computer processes data")

co = Computer()
co.work() 

#15
class Game(ABC) :
     @abstractmethod
     def play(self):
        pass

class Cricket(Game) :
    def play(self):
        print("Cricket is played with bat and ball")

cr = Cricket()
cr.play() """




