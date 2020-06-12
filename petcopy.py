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

    def strengths(self):
        if self.typeof == "fire" and Monster.typeof == "tree":
            self.attack *2 and Monster.health/2
       
    def weaknesses(self):
        pass

    def healing(self):
        self.health += 50

    def potion(self):
        self.exp_pt += self.roll(0,5) * 3
        
        if self.exp_pt == 100:
            ("You are evolving!")

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
        monsterID = 1
        if monsterID == 1:
            monster = TreeMonster()
        in_battle = True
        print("Time to fight," + " " + self.name+"!")
        print(monster.name +" " + "is attacking!")
        while in_battle:
            if self.typeof == monster.weakagainst:
                thisattack = self.roll(0,10) * 2
                thatattack = self.roll(0,5)
            monster.health -= thisattack
            self.health -= thatattack
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





#main()



tama = Pet("Tama", "fire", 15, 15, 0)
#laila = Healer("Laila", "healer", 25, 5, 5)

print(tama)
#tama.encounter()
#print(tama)
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