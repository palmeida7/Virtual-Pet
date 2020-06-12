import random

class Pet:   
    def __init__(self, name, typeof, health, attack, exp_pt):
        self.name = name 
        self.typeof = typeof
        self.health = health
        self.attack = attack
        self.exp_pt = exp_pt
    
    def roll(self, min, max):
        roll = random.randint(min,max)
        return roll

    def healing(self):
        self.health += 50

    def potion(self):
        self.exp_pt += self.roll(0,5)
        
        if self.exp_pt == 100:
            ("You are evolving!")

##hunting replenishes your health
    def hunt(self):
        print("Shall we hunt," +" " + self.name +"?")
        self.health += self.roll(0,20)
        self.attack += self.roll(0,10)
        self.exp_pt += self.roll(0,5)

##encounters a monster that may deal you damage
    def encounter(self):
        print("Flight or fight," + " " + self.name+"!")
        self.attack += self.roll(0,10)
        self.exp_pt += self.roll(0,10)
        if self.attack < 5:
            self.health -= 5

    def train(self):
        self.attack += self.roll(0,5)
        self.exp_pt += self.roll(0,5)
        
    def sleep(self):
        self.health += self.roll(0,5)

    def evolve(self):
        print("This is gonna hurt a little bit!")
        self.health -= self.roll(0,10)
        self.attack += self.roll(0,10)
        self.exp_pt -= self.roll(0,10)

    def sing(self):
        print("Sing for me, " + self.name + "!")
        print(self.name +": " + "La, la, la, la, la, la!")
        print("Okay, that's too much.")

    def __str__(self):
        return """
        %s:
        typeof: %s
        health: %d
        attack: %d
        exp_pt: %d
        """ % (self.name, self.typeof, self.health, self.attack, self.exp_pt) 


class Healer(Pet):
    def __init__(self, name, typeof, health, attack, exp_pt):
        self.name = name 
        self.typeof = typeof
        self.health = health
        self.attack = attack
        self.exp_pt = exp_pt
        

    def heal(self, other_pet):
        self.heal = heal
        for i in range(self.heal):
            other_pet.healing()

class Monster(Pet):
    def __init__(self):
        super().__init__()
        pass




#main()



tama = Pet("Tama", "fire", 15, 15, 0)
#laila = Healer("Laila", "healer", 25, 5, 5)
print(tama)
""" tama.hunt()
print(tama)
tama.encounter()
print(tama)
tama.train()
print(tama)
tama.sleep()
print(tama)
tama.sing()
print(tama)
tama.potion()
print(tama) """