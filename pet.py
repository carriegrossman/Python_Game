class Pet():
    def __init__(self, name, fullness=50, energy=50, purr_happiness=85, hunger=5, sad=5):
        self.name = name
        self.fullness = fullness
        self.energy = energy
        self.purr_happiness = purr_happiness
        self.hunger = hunger
        self.sad = sad

    def get_love(self):
        self.purr_happiness +=10 
    
    def eat_food(self):
        self.fullness += 30
    
    def nap_time(self):
        self.energy += 50
    
    def life(self):
        self.fullness -= self.hunger
        self.purr_happiness -= self.sad

#subclass of class Pet
class PlayfulPet(Pet):
    def __init__(self, name, fullness=50, energy=50, hunger=5, play_level=1):
        super().__init__(name, fullness, energy, 100, hunger, 1)
        self.play_level = play_level
    
    def life(self):
        self.fullness -= self.hunger
        self.purr_happiness -= self.sad/2
    
    def play(self, other_cat):
        #Super play powers
        for i in range(self.play_level):
            other_cat.get_love()


# dexter = Pet("Dexter", 50, 50, 85, 5, 5)
# sushi = PlayfulPet("Sushi", 65, 70, 95, 3)

# print(dexter.purr_happiness)
# sushi.play(dexter)
# print(dexter.purr_happiness)