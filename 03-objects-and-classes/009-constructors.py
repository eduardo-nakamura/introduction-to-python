# https://python.land/objects-and-classes/python-constructors
class Car:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Car Started")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrum")
        else:
            print("Start the car first")
    
    def stop(self):
        self.speed = 0

c1 = Car()
c2 = Car(True)
c3 = Car(True, 50)
c4 = Car(started = True, speed = 40)

