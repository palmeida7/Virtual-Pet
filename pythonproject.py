##Premise of the game a virtual pet that you raise
##ability to fight other monsters
##multiple inputs

class virtual_pet:   
    def __init__(self, name, typeof, health):
        self.name = name 
        self.typeof = typeof
        self.health = health


    def hunt(self):
        print("Shall we hunt," +" " + self.name +"?")
        self.health += 20

    #def 

tama = virtual_pet("Tama", "fire", 10)
print(tama)

tama.hunt()
print(tama.health)