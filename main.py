from pet import Pet, PlayfulPet
from toy import Toy

pets = []

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
    choice_string += "Please choose an option: \n"
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

def main():    
    while True:
        choice = get_user_choice(main_menu)
        if choice == 1:
            pet_name = input("Please enter the name of your new pet: \n")
            print("What type of pet would you like to adopt? \n")
            type_choice = get_user_choice(adoption_menu)
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(PlayfulPet(pet_name))
                print("Extra playful! \n")
            print("You now have %d pets" % len(pets))
        if choice == 2:
            for pet in pets:
                pet.get_love()
        # if choice == 3:
            

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
            exit()
    
main()