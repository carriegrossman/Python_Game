class Pet():
    def __init__(self, name):
        self.name = name
        self.hunger = 15
        self.energy = 45
        self.purr_happiness = 85

    def play(self):
        self.energy -=15

    def get_cuddles(self):
        self.purr_happiness +=10 
    
    def eat_food(self):
        self.energy += 10
        self.hunger -= 20


dexter = Pet("Dexter")
dexter.play()
print(dexter.energy)
dexter.get_cuddles()
print(dexter.purr_happiness)