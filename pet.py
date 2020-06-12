class Pet():
    def __init__(self, name, fullness=50, energy=60, happiness=75, hunger=50, sad=5):
        self.name = name
        self.fullness = fullness
        self.energy = energy
        self.happiness = happiness
        self.hunger = hunger
        self.sad = sad
        self.toys = []

    def get_love(self):
        self.happiness +=20
        self.energy -= 15
        self.hunger += 10
        self.fullness -= 10
    
    def eat_food(self):
        self.fullness += 15
        self.hunger -= 10
    
    def nap_time(self):
        self.energy += 25
        self.fullness -= 10
    
    def life(self):
        self.fullness -= self.hunger
        self.happiness -= self.sad
        for toy in self.toys:
            self.happiness += toy.use()
        for treat in self.treats:
            self.happiness += treat.give_treat()
        for treat in self.treats:
            self.fullness += treat.give_treat()
    
    def get_toy(self, toy):
        self.toys.append(toy)
        self.happiness += 10
        self.energy -= 5

    def __str__(self):
        return """
        %s
        Energy: %d
        Happiness: %d
        Hunger: %d
        Fullness: %d
        """ % (self.name, self.energy, self.happiness, self.hunger, self.fullness)

#subclass of class Pet
class PlayfulPet(Pet):
    def __init__(self, name, fullness=50, energy=95, hunger=50, play_level=1):
        super().__init__(name, fullness, energy, 100, hunger, 1)
        self.play_level = play_level
    
    def life(self):
        self.fullness -= self.hunger
        self.happiness -= self.sad/2
        for toy in self.toys:
            self.happiness += toy.use()
        for treat in self.treats:
            self.happiness += treat.give_treat()
        for treat in self.treats:
            self.fullness += treat.give_treat()
    
    def play(self, other_pet):
        #Super play powers
        for i in range(self.play_level):
            other_pet.get_love()



# dexter = Pet("Dexter", 50, 50, 85, 5, 5)
# sushi = PlayfulPet("Sushi", 65, 70, 95, 3)

# print(dexter.purr_happiness)
# sushi.play(dexter)
# print(dexter.purr_happiness)