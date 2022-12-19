class Vehicle:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Started")

    def stop(self):
        self.speed = 0

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrum")
        else:
            print("Start first")

# Class car inherit from Class Vehicle
class Car(Vehicle):
    trunk_open = False

    def open_trunk(self):
        self.trunk_open = True
    def close_trunk(self):
        self.trunk_open = False

# Overriding Python methods
class Motorcycle(Vehicle):
    def __init__(self, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__()

# Overriding other methods
class Motorcycle2(Vehicle):
    def __init__(self, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__()
    def start(self):
        print("Sorry, out of fuel")


