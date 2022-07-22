# Jonathan Fulkerson
# SDEV 220
# Module 3 Lab
# 7/21/22

class Vehicle:
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

class Automobile(Vehicle):
    def __init__(self):
        #Vehicle.__init__(self, year, make, model, doors, roof)
        super().__init__(year, make, model, doors, roof)

print("Enter the attributes of the car you would like to add")
type = "car"
year = input("Year: ")
make = input("Make: ")
model = input("Model: ")
doors = input("Doors(2 or 4): ")

while doors not in ("2", "4"):
    print("You did not input a valid value for the amount of doors. Enter only 2 or 4")
    doors = input("Doors (2 or 4): ")

roof = input("Roof (solid or sun roof): ")

while roof not in ("solid", "sun roof"):
    print("You did not enter a valid value for the roof type. Enter only solid or sun roof")
    roof = input("Roof (solid or sun roof): ")

user_car = Automobile()
print()
print(f"Vehicle type: {type}\nYear: {user_car.year}\nMake: {user_car.make}\nModel: {user_car.model}\nNumber of doors: {user_car.doors}\nType of roof: {user_car.roof}")
