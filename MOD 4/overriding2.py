class Person:
    def description(self):
        print('Hello I am a person')

class Employee(Person):
    def description(self):
        print('Hello I am an Employee')

class Landlord(Person):
    def description(self):
        print('Hello I am a LandLord')

a = Person()
a.description()
b = Employee()
b.description()
c = Landlord()
c.description()