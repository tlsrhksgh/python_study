
class Car:
    def __init__(self):
        self.wheels = 4
    
    def drive(self):
        print("drive")

mycar = Car()

getattr(mycar, "wheels")

method = getattr(mycar, "drive")
method()