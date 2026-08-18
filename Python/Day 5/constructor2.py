class People:
    def __init__(self, name, fav_food, walk): # parameterized constructor 
        self.name = name                      # Python only supports one constructor/init method per class.
        self.fav_food = fav_food
        self.walk = walk 
        
    def get_walk(self):
        return self.walk # a method to perform a function
        

p1 = People("John", "Biryani", 50)
p2 = People("Ravi", "Potato", 80)

# print(p1.name, p1.fav_food, p1.walk)
# print(p2.name, p2.fav_food, p2.walk)

print(f"{p1.name} has walked {p1.get_walk()} Km in a day!")
print(f"{p2.name} has walked {p2.get_walk()} Km in a day!")
