from petcopy import Pet

tama = Pet("Tama", "fire", 15, 15, 0)

main_menu = [   
    "Hunt",
    "Encounter",
    "Train",
    "Sleep",
    "Evolve",
    "Sing",
    "View status of pets",
    "Exit program",
]

def print_menu_error():
    print("That was not a valid choice. Try again.\n\n\n")    

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += "Please choose an option:\n "
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
            if tama.health >= 0:
                tama.hunt()
                print(tama)
            elif tama.health <= 0:
                print("Come on...do something.")  
        if choice == 2:
            if tama.health >= 0:
                tama.encounter()
                print(tama)
            elif tama.health <= 0:
                print(tama.name + "is ded. D-E-D, ded.")
        if choice == 3:
            if tama.health >= 0:
                tama.train()
                print(tama)
            elif tama.health <= 0:
                print("I'm prettttty sure it can't do anything.")             
        if choice == 4:
            if tama.health >= 0:
                tama.sleep()
                print(tama)
            elif tama.health <= 0:
                print("Hello? Are you alive.")  
        if choice == 5:
            if tama.health >= 0:
                tama.evolve()
                print(tama)
            elif tama.health <= 0:
                print("Come on...do something.")  
        if choice == 6:
            if tama.health >= 0:
                tama.sing()
                print(tama)
            elif tama.health <= 0:
                print("Come on...do something.")  
        if choice == 7:
            if tama.health >= 0:
                print(tama)
            elif tama.health <= 0:
                print("Come on...do something.")  
        if choice == 8:
            print("Thank you for playing!")
            exit()


main()
