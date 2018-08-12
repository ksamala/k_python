class Dog():
    def __init__(self,name):
        self.name = name

    def Action(self):
        return self.name + " barks"

class Cat():
    def __init__(self,name):
        self.name = name

    def Action(self):
        return self.name + " purr"

ace = Dog("Ace")
flex = Cat("flex")
    
def pet_speak(pet):
    return pet.Action()
print(pet_speak(ace)) 