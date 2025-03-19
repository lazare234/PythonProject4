class Car:
    def __init__(self, make="toyota", model="Camry", year=2020, milage=100):
        self.make = make
        self.model = model
        self.year = year
        self.milage = milage

    def __str__(self):
        print(f"This is a {self.make} car, its modes is {self.model}, it is released in {self.year}, and its milage is{self.milage}")
    def upgrade_milage(self):
        update = int(input("update your cars milage by:"))
        if update > 0:
            self.milage += update
        else:
            print("sorry you cant make any changes")
    def calculate_car_year(self):
        now_year = 2025
        print(now_year - self.year)

car1 = Car("toyota", "Camry", "2020", "100")
print(car1)





