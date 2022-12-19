# An object is a collection of data (variables) and methods that operate on that data. 
# Objects are defined by a Python class.

# A class is the blueprint for one or more objects

# type('a') <class 'str'>
# type(1) <class 'int'>
# type(True) <class 'bool'>

class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True
        print("Car started, let's ride!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrum")
        else:
            print("Start the car first")

    def stop(self):
        self.speed = 0
        print("Stop")

car = Car()
car.increase_speed(10) # Start the car first
car.start() # Car Started
car.increase_speed(40) # Vrum

car1 = Car()
car2 = Car()
print(id(car1)) # show id car1
print(id(car2)) # show id car2

car1.start()
car1.increase_speed(10)
print("Car 1 Speed:", car1.speed, "\nCar 2 Speed:", car2.speed)