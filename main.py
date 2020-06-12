from pet import Pet, PlayfulPet
from toy import Toy
from treats import Treat

pets = []

print("Welcome Virtual Pet Game 🐶!\n ")

main_menu = [
    "Adopt a Pet",
    "Play with Pet",
    "Treat!",
    "Feed Pet",
    "Nap time!",
    "View Pet's Status",
    "Give a toys to your pets",
    "Do nothing",
    "Exit"
]

def print_menu_error():
    print("That choice was invalid. Please try again. \n")

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += "\n Please choose an option: \n"
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

adoption_menu = [
    "Pet",
    "Playful Pet"
]

treat_list = [
    Treat("Steak",2,4, "I love steak!"),
    Treat("Bacon",1,2,"This is delish!"),
    Treat("Surprise Treat",2,1, "Yum!")
]

def treats_to_string(treat_list):
    treat_string = ""
    num = 1
    for treat in treat_list:
        treat_string += "%d: %s\n" % (num, treat.name)
        num += 1
    treat_string += "\n Give your pet a treat: \n"
    return treat_string

def get_pet_treat(treat_list):
    treat = -1
    treat_string = treats_to_string(treat_list)
    while treat == -1:
        try:
            treat= int(input(treat_string))
            if treat <= 0 or treat > len(treat_list):
                raise ValueError
        except ValueError:
            print_menu_error()
    return treat

def main():    
    while True:
        choice = get_user_choice(main_menu)
        if choice == 1:
            pet_name = input("\n Please enter the name of your new pet: \n")
            print("\n What type of pet would you like to adopt? \n")
            type_choice = get_user_choice(adoption_menu)
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(PlayfulPet(pet_name))
                print("Extra playful! \n")
            print("You now have %d new pet(s) \n" % len(pets))
        if choice == 2:
            for pet in pets:
                pet.get_love()
        if choice == 3:
            print("What kind of treat would you like to give your pet? \n")
            for pet in pets:
                type_treat = get_pet_treat(treat_list)
                my_treat = treat_list[type_treat]
                print(my_treat.message)
                results = my_treat.give_treat()
                pet.happiness += results[1]
                pet.hunger -= results[0]
        if choice == 4:
            for pet in pets:
                pet.eat_food()
        if choice == 5:
            for pet in pets:
                pet.nap_time()
        if choice == 6:
            for pet in pets:
                print(pet)
        if choice == 7:
            for pet in pets:
                pet.get_toy(Toy())
        if choice == 8:
            for pet in pets:
                pet.life()
        if choice == 9:
            exit(print("Bye for now!"))
    
main()