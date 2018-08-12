class Animal():

    def __init__(self):
        print("A1")

    def eat(self):
        print("A2")

class Dog(Animal): # inherit animal class

    def __init__(self):
        Animal.__init__(self)
    
    # def eat(self):   # If same method is defined, then it overwrites parent class mehod. 
    #     print("E1")       

    def who_am_i(self):
        print("D2")

mydog = Dog()
eat = mydog.eat()
who = mydog.who_am_i()


