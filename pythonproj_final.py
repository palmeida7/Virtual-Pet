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

    def __str__(self):
        return """
        %s:
        typeof: %s
        health: %d
        attack: %d
        exp_pt: %d
        """ % (self.name, self.typeof, self.health, self.attack, self.exp_pt) 

    def print_menu_error():
        print("That was not a valid choice. Please try again. \n\n\n")

    def choices_to_string(choice_list):
        choice_string = ""
        num = 1
        for choice in choice_list:
            choice_string += "%d: %s\n" % (num, choice)
            num += 1
        choice_string += "Please choose an option: "
        return choice_string

    def get_user_choice(choice_list):
        choice = -1
        choice_string = choices_to_string(choice_list)
        while choice == -1:
            try:
                choice = int(input(choice_string))
                if choice <= 0 or choice > len(choice_list):
                    raise ValueError
            except ValueError:
                print_menu_error()
        return choice

    def main():    
        while True:
            choice = get_user_choice(main_menu)
            if choice == 1:
                pet_name = input("What would you like to name your pet? ")
                pets.append(Pet(pet_name))
                print("You now have %d pets" % len(pets))

            if choice == 4:
                for pet in pets:
                    print(pet)
            
#virtual_pet.main()



tama = virtual_pet("Tama", "fire", 10, 5, 0)
#print(tama)
