# Question 1: Defining a class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h.")

# Inherited class: Car
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def move(self):
        print(f"{self.brand} is driving on the road 🚗 at {self.speed} km/h with {self.fuel_type} fuel.")

# Inherited class: Plane
class Plane(Vehicle):
    def __init__(self, brand, speed, altitude):
        super().__init__(brand, speed)
        self.altitude = altitude  # in meters

    def move(self):
        print(f"{self.brand} is flying in the sky ✈️ at {self.speed} km/h at {self.altitude} meters altitude.")

# Inherited class: Boat
class Boat(Vehicle):
    def __init__(self, brand, speed, boat_type):
        super().__init__(brand, speed)
        self.boat_type = boat_type

    def move(self):
        print(f"{self.brand} is sailing on the water 🚢 at {self.speed} km/h as a {self.boat_type}.")

# Demonstrating Polymorphism
def show_movement(vehicles):
    for v in vehicles:
        v.move()

# Create objects
car = Car("Toyota", 120, "Gasoline")
plane = Plane("Boeing", 900, 10000)
boat = Boat("SeaRay", 40, "Yacht")

# Run polymorphic behavior
vehicle_list = [car, plane, boat]
show_movement(vehicle_list)
# Base class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed  # speed in km/h

    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h.")

# Inherited class: Car
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def move(self):
        print(f"{self.brand} is driving on the road 🚗 at {self.speed} km/h with {self.fuel_type} fuel.")

# Inherited class: Plane
class Plane(Vehicle):
    def __init__(self, brand, speed, altitude):
        super().__init__(brand, speed)
        self.altitude = altitude  # in meters

    def move(self):
        print(f"{self.brand} is flying in the sky ✈️ at {self.speed} km/h at {self.altitude} meters altitude.")

# Inherited class: Boat
class Boat(Vehicle):
    def __init__(self, brand, speed, boat_type):
        super().__init__(brand, speed)
        self.boat_type = boat_type

    def move(self):
        print(f"{self.brand} is sailing on the water 🚢 at {self.speed} km/h as a {self.boat_type}.")

# Demonstrating Polymorphism
def show_movement(vehicles):
    for v in vehicles:
        v.move()

# Create objects
car = Car("Toyota", 120, "Gasoline")
plane = Plane("Boeing", 900, 10000)
boat = Boat("SeaRay", 40, "Yacht")

# Run polymorphic behavior
vehicle_list = [car, plane, boat]
show_movement(vehicle_list)

## Activity 2: Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")

# Subclasses with different implementations
class Dog(Animal):
    def move(self):
        print(f"{self.name} is running 🐕.")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming 🐟.")

class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying 🐦.")

# Demonstrate polymorphism
animals = [Dog("German"), Fish("Nemo"), Bird("Goose")]
for animal in animals:
    animal.move()
