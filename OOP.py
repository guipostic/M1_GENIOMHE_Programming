# Define a class (blueprint)
class Car:
    def __init__(self, make, color):
        """
        Special method
        Runs automatically when you create a new object from a class
        Often used to set up the initial state of an object
        """
        self.make = make      # attribute
        self.color = color    # attribute
        self.speed = 0        # default attribute

    def drive(self, mph):     # method
        self.speed = mph
        print(f"The {self.color} {self.make} is now going {self.speed} mph.")

    def brake(self):          # method
        self.speed = 0
        print(f"The {self.color} {self.make} has stopped.")

class ElectricCar(Car):  # inherits from Car
    def charge(self):
        print(f"The {self.color} {self.make} is charging.")

class Bike:
    def __init__(self, make, color):
        self.make = make      # attribute
        self.color = color    # attribute
        self.speed = 150        # default attribute

    def brake(self):          # method
        self.speed /= 10
        print(f"The {self.color} {self.make} is now going {self.speed} mph (10x slower)")


# Create objects (instances of Car)
my_car = Car("Toyota", "blue")
friend_car = Car("Honda", "red")

# Use methods
my_car.drive(60)
friend_car.brake() # NOTE: "self" is the name Python gives to the current object instance

# Class inheritance
new_car = ElectricCar("Nissan", "green")
new_car.charge()

# Polymorphism: different classes can define the same method, but behave differently.
my_bike = Bike("Kawazaki", "black")
my_bike.brake()

