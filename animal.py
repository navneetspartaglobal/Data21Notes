class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breath(self):
        print("one breath in and one out")

    def eat(self):
        print("eat sweet dish")

    def moving(self):
        print("forward, backward and everywhere")


cat = Animal()
cat.breath()
print(__name__)

