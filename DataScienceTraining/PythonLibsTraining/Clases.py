class Employee:
    # Atteibutes
    empCount = 0

    # Methods

    # Construtor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print(Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name, " and Salary:", self.salary)


emp1 = Employee('Muhammad', 31)
emp2 = Employee('Koko', 55)

emp1.displayCount()
emp2.displayCount()

emp1.displayEmployee()
emp2.displayEmployee()

emp1.age = 5
print(emp1.age)

delattr(emp1, 'age')
#print(emp1.age)

print("*" * 50)
# ////////\\\\\\\\////////\\\\\\\


class Vehicle:

    color = 'White'

    def __init__(self, type):
        print("Vehicle type is", type)

    def move(self, speed):
        print("This vehicle can move with a %s speed/hour." % speed)

    def setColor(self, color):
        self.color = color

    def getColor(self):
        print("This vehicle's color is:", self.color)

    def fuel(self):
        print('Use diesel.')


class Plane(Vehicle):

    def __init__(self):
        print("This is a Plane.")

    def fly(self, flySpeed):
        print('This plane can fly with: {} Km/h'.format(flySpeed))

    def fuel(self):
        print("Planes use Petrol.")



car1 = Vehicle('VolksWagen')
car1.getColor()
car1.setColor("Brown")
car1.getColor()
car1.move(220)
car1.fuel()

print('/'*20, '\\'*20)
Jumbo = Plane()
Jumbo.fly(350)
Jumbo.fuel()
Jumbo.getColor()







