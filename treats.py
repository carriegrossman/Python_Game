class Treat():
    def __init__(self, name, food_value=5, fun=10, message=" "):
        self.name = name
        self.food_value = food_value
        self.fun = fun
        self.message = message
    
    def give_treat(self):
        return [self.food_value, self.fun]