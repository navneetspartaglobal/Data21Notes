class AmazingDog:

    animal_kind = "canine"

    def bark(self):
        print(self.animal_kind)
        return "woof!"


Bob = AmazingDog()

Bob.animal_kind = "dolphin"
print(Bob.animal_kind)


class AmazingDog:

    def bark(self):
        print(self.animal_kind)
        return "woof!"


Bob = AmazingDog()

Bob.animal_kind = "dolphin"
print(Bob.animal_kind)


