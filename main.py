from pet import Pet, PlayfulPet
from toy import Toy
from treats import Treat

pets = []

print(u"\u001b[46;1m Welcome Virtual Pet Game! \u001b[0m\n")

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
    print(u"\u001b[41m That choice was invalid. Please try again. \u001b[0m\n")

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += u"\n\u001b[36;1m Please choose an option: \u001b[0m\n"
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
    Treat("Steak",3,7, u"\u001b[35;1m I love steak!\u001b[0m"),
    Treat("Bacon",2,5,u"\u001b[35;1m This is delish! \u001b[0m"),
    Treat("Surprise Treat",2,6, u"\u001b[35;1m YUUMM! \u001b[0m")
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
            pet_name = input(u"\n\u001b[32;1m Please enter the name of your new pet: \u001b[0m\n")
            print(u"\u001b[35;1m\n What type of pet would you like to adopt? \u001b[0m\n")
            type_choice = get_user_choice(adoption_menu)
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(PlayfulPet(pet_name))
                print(u"\n\u001b[35;1m Extra playful! \u001b[0m\n")
            print("You now have %d new pet(s) \n" % len(pets))
        if choice == 2:
            for pet in pets:
                pet.get_love()
            print(u"\u001b[32;1mThis is fun! Let's play all day\u001b[0m")
        if choice == 3:
            print(u"\n\u001b[32;1m What kind of treat would you like to give your pet? \u001b[0m\n")
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
            print(u"\u001b[32;1m YUM! That hit the spot! \u001b[0m")
        if choice == 5:
            for pet in pets:
                pet.nap_time()
            print(u"\u001b[32;1m I need a nap...I'm sleepy. \u001b[0m")
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
            exit(print(u"\u001b[42m Bye for now! \u001b[0m\n"))
    
main()