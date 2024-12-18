class monkey:
    def __init__(self, name1):
        self.name = name1
    def walk(self):
        print(self.name +" is walking")
    def attack(self):
        print(self.name + " is attacking")           
    def think(self):
        print(self.name + " is thinking") 


class human(monkey):
    def __init__(self, name1):
        super().__init__(name1)
    def big_think(self):
        print(self.name + " is big_thinking")



b1 = human("HUMAN1")
b1.walk()
b1.attack()
b1.think()
b1.big_think()

#b1 = ("Human2")
#b1.
#b1.
#b1.
#b1.
#class human:
#    def __init__(self, name1, age1):
#        self.name = name1
#        self.age = age1
#        self.a = 4
#    def breath(self):
#        print(self.name + " is breathing")
#    def walk(self):
#        print(self.name + " is walking")
#    def getFullHumanInformation(self):
#        return self.name + "  " + self.age
#
#a = human("Serhii", 18)
#a.breath()
#a.walk()
#
#a = human("Vova", 19)
#a.breath()
#a.walk()



