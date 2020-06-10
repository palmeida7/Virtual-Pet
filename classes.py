class Character():
#for every method inside the class, the first parameter required is "self"
    #def __init__(self, name, position, speed = 10, health=100, attack_power=5):
    def __init__(self, name, position, speed, health, attack_power):    
        self.name = name
        self.health = health                    
        self.speed = speed
        self.position = position
        self.attack_power = attack_power

    def attack(self, char):
        char.health -=self.attack_power

#init == initiate
    def move(self, dir):
        if dir == "right":
            self.position["x"] += speed
        elif dir == "left":
            self.position["x"] -= speed
        elif dir == "up":
            self.position["y"] -= speed
        elif dir == "down":
            self.position["y"] += speed


class Player(Character):
    def heal(self):
        self.health += 25

class Enemy(Character):
    def __init__(self, name, position):
        super().__init__(name, position) #inherits everything from the parent
        self.health = 50
        self.speed = 4
        """ print("This is doing something")
        self.name = name
        self.health = health                    
        self.speed = speed
        self.position = position """

    def roll(self):
        self.position["x"] -=25


##example
##""" enemy1 = Enemy("Bad Guy", {"x":20,"y":100})
##player1 = Player("Clint", {"x":10,"y":200}, 140, 1000, 35)

##while player1.health > 300:
##    enemy1.attack(player1)
#    print(player1.health) """


