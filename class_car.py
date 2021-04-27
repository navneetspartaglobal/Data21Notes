"""Create a car class.
Give the vehicle a maximum speed,
and keep track of the current speed of the vehicle.
It doesn't make sense for the speed to be adjusted directly,
so put an underscore in front of it and implement a speed getter as well as accelerate
and brake setter methods that change the speed in a logical way.

Do your methods make sense? Does braking past 0 cause the speed to increase? Can you accelerate past the car's top speed? """

class Car:

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def specs(self, speed):
        print(self.speed)


obj = Car(10, 'red')

obj.specs(10)


