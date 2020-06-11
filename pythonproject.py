##Premise of the game a virtual pet that you raise
##ability to fight other monsters
##multiple inputs
import random

pets = []

main_menu = [
    "hunt",
    "encounter",
    "train",
    "sleep",
    "evolve",
    "sing",
    "status"
]

class virtual_pet:   
    def __init__(self, name, typeof, health, attack, exp_pt):
        self.name = name 
        self.typeof = typeof
        self.health = health
        self.attack = attack
        self.exp_pt = exp_pt

    def roll(self, min, max):
        roll = random.randint(min,max)
        return roll

   
    #def turn(self):
        print("menu:")
        print("1.hunt")
        print("  ******")
        print("2.encounter")
        print("  ******")
        print("3.train")
        print("  ******")
        print("4.sleep")
        print("  ******")
        print("5.evolve")
        print("  ******")
        print("6.sing")
        print("  ******")
        print("7.status")
        input("What shall we do " + self.name +"?\n")
        if input == 1:
            self.hunt()
        if input == 2:
            self.encounter()
        if input == 3:
            self.train()
        if input == 4:
            self.sleep()
        if input == 5:
            self.evolve()
        if input == 6: 
            self.sing() 
    
    def git_status(self):
        print(tama)

    def exp_pt(self):
        pass
        #if self.exp_pt == 100:

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
        self.exp_pt -= self.roll(0,20)

    def sing(self):
        print("Sing for me, " + self.name + "!")
        print(self.name +": " + "La, la, la, la, la, la!")
        print("Okay, that's too much.")

    def __str__(self):
        return """
        %s:
        typeof: %d
        health: %d
        attack: %d
        exp_pt: %d
        """ % (self.name, self.typeof, self.health, self.attack, self.exp_pt) 

  """   #def start(self):
        playing = True
        while playing:
            if tama.health > 0:
                tama.turn()
            ##This goes to menu. stop while loop and jump to other functions
            if tama.health <= 0:
                playing = False
                print(self.name + "ded yall. D-E-D, ded.") """
    


tama = virtual_pet("Tama", "fire", 10, 5, 0)
print(tama)

#tama.start()



""" class Monster1(virtual_pet):
    self.health = 20
    self.attack = 5

class Treemon(virtual_pet):
    self.health = 30
    self.attack = 10 """



""" tama.hunt()
print(tama.health) """

#tama.encounter()

#print(tama.sing())