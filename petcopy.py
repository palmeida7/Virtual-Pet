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

  
##hunting replenishes your health
    def hunt(self):
        print("Shall we hunt," +" " + self.name +"?")
        self.health += self.roll(0,20)
        self.attack += self.roll(0,10)
        self.exp_pt += self.roll(0,5)

##encounters a monster that may deal you damage
#enemy will appear in encounter. how to do that in function
#how to know if you are in a battle
#how do we know when battle is still going? till death or flee?
#do we want loot?
    def encounter(self):
        #monsterID = 1
        monsterID = self.roll(1,2)
        if monsterID == 1:
            monster = TreeMonster()
        if monsterID == 2:
            monster = WaveMonster()
        in_battle = True
        print("Time to fight," + " " + self.name+"!")
        print(monster.name +" " + "is attacking!")
        while in_battle:
            if self.health == 5:
                potion = self.roll(5,10)
                self.health += potion
            if self.typeof == monster.weakagainst:
                thisattack = self.roll(0,10) * 1
                thatattack = self.roll(0,5) * (0.75)
                monster.health -= thisattack
                self.health -= thatattack
            if self.typeof == monster.strongagainst:
                thisattack = self.roll(0,10) * 1
                thatattack = self.roll(0,5) * (0.75)
                monster.health -= thatattack
                self.health -= thisattack
            if monster.health <= 0 or self.health <=0:
                in_battle = False
            print("Monster HP: ")
            print(monster.health)
            print("Tama HP: ")
            print(self.health)
            if self.typeof != monster.weakagainst:
                thisattack = self.roll(0,10)
            self.exp_pt += self.roll(0,10)
        
     
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


#class Healer(Pet):
#    def __init__(self, name, typeof, health, attack, exp_pt):
#        self.name = name 
#        self.typeof = typeof
#        self.health = self.roll(0,5)
#        self.attack = attack
#        self.exp_pt = exp_pt
        

#    def heal(self, other_pet):
#        self.heal = heal
#        for i in range(self.heal):
#            other_pet.healing()

class Monster(Pet):
    def __init__(self, name, typeof, health, attack, exp_pt, weak, strong):
        #super().__init__()
        self.name = name
        self.typeof = typeof
        self.health = health
        self.attack = attack
        self.exp_pt = exp_pt
        self.weakagainst = weak
        self.strongagainst = strong
class TreeMonster(Monster):
    def __init__(self):
        super().__init__("Tree", "tree", 15, 15, 0, "fire", "water")
class WaveMonster(Monster):
    def __init__(self):
        super().__init__("Wave", "wave", 15, 15, 0, "tree", "fire")







tama = Pet("Tama", "fire", 15, 15, 0)

print(tama)
