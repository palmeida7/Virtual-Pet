

class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
    
    
    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)    

benji = Pet("Benji", 50, 20, 20, 1)
lassie = Pet("Lassie", 50, 20, 20, 1)
clifford = Pet("Old Yeller", 50, 20, 20, 1)

print(lassie)