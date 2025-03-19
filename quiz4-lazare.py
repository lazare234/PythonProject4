#davaleba2

# class Ticket:
#     def __init__(self, title, price, quantity, language="Geo"):
#         self.title = title
#         self.price = price
#         self.quantity = quantity
#         self.language = language
#
#     def __str__(self):
#         return f"Movie: {self.title}, Price: {self.price} GEL, Tickets Left: {self.quantity}, Language: {self.language}"
#
#     def __lt__(self, other):
#         return self.quantity < other.quantity
#
#
# class User:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance
#
#     def __str__(self):
#         return f"User: {self.name}, Balance: {self.balance} GEL"
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"{amount} GEL has been added to {self.name}'s balance.")
#         else:
#             print("Invalid deposit amount.")
#
#
#
# ticket = Ticket(title="Avengers: Endgame", price=25, quantity=100)
#
# user = User(name="John Doe", balance=100)
# user1 = User(name="Nicholas Jackson", balance=200)
# user2 = User(name="Jasurbeki Yakhshiboev", balance=150)
# user3 = User(name="Cristiano Ronaldo", balance=1000)
# user4 = User(name="Liones Pepsi", balance=25)
# print(user)
# print(user1)
# print(user2)
# print(user3)
# print(user4)
# print("--------------------------------------------------------")
# print(ticket)
# print("--------------------------------------------------------")
# user.deposit(50)
# user1.deposit(50)
# user2.deposit(15)
# user3.deposit(150)
# user4.deposit(200)
# print("--------------------------------------------------------")
# print(user)
# print(user1)
# print(user2)
# print(user3)
# print(user4)

#davaleba1
with open('titanic.txt', 'r') as file:
    lines = file.readlines()

lines = lines[1:]


total_passengers = 0
female_count = 0
male_count = 0
female_survived = 0
female_died = 0
male_survived = 0
male_died = 0
class_1_count = 0
class_2_count = 0
class_3_count = 0
class_1_price_sum = 0
class_2_price_sum = 0
class_3_price_sum = 0


for line in lines:
    data = line.strip().split(',')


    if len(data) < 12:
        continue

    try:
        passenger_id = int(data[0])
        survived = int(data[1])
        ticket_class = int(data[2])
        sex = data[4].strip().lower()
        ticket_price = float(data[9])
    except ValueError:
        continue


    total_passengers += 1

     
    if sex == "female":
        female_count += 1
        if survived == 1:
            female_survived += 1
        else:
            female_died += 1
    elif sex == "male":
        male_count += 1
        if survived == 1:
            male_survived += 1
        else:
            male_died += 1

    if ticket_class == 1:
        class_1_count += 1
        class_1_price_sum += ticket_price
    elif ticket_class == 2:
        class_2_count += 1
        class_2_price_sum += ticket_price
    elif ticket_class == 3:
        class_3_count += 1
        class_3_price_sum += ticket_price


female_percentage = (female_count / total_passengers) * 100 if total_passengers > 0 else 0
male_percentage = (male_count / total_passengers) * 100 if total_passengers > 0 else 0


female_survival_percentage = (female_survived / female_count) * 100 if female_count > 0 else 0
female_death_percentage = (female_died / female_count) * 100 if female_count > 0 else 0


male_survival_percentage = (male_survived / male_count) * 100 if male_count > 0 else 0
male_death_percentage = (male_died / male_count) * 100 if male_count > 0 else 0


class_1_percentage = (class_1_count / total_passengers) * 100 if total_passengers > 0 else 0
class_2_percentage = (class_2_count / total_passengers) * 100 if total_passengers > 0 else 0
class_3_percentage = (class_3_count / total_passengers) * 100 if total_passengers > 0 else 0


avg_class_1_price = class_1_price_sum / class_1_count if class_1_count > 0 else 0
avg_class_2_price = class_2_price_sum / class_2_count if class_2_count > 0 else 0
avg_class_3_price = class_3_price_sum / class_3_count if class_3_count > 0 else 0


result = {
    "Total Passengers": total_passengers,
    "Female Count": female_count,
    "Female Percentage": female_percentage,
    "Male Count": male_count,
    "Male Percentage": male_percentage,
    "Female Survived": female_survived,
    "Female Survival Percentage": female_survival_percentage,
    "Female Death Percentage": female_death_percentage,
    "Male Survived": male_survived,
    "Male Survival Percentage": male_survival_percentage,
    "Male Death Percentage": male_death_percentage,
    "Class 1 Count": class_1_count,
    "Class 1 Percentage": class_1_percentage,
    "Class 2 Count": class_2_count,
    "Class 2 Percentage": class_2_percentage,
    "Class 3 Count": class_3_count,
    "Class 3 Percentage": class_3_percentage,
    "Avg Class 1 Price": avg_class_1_price,
    "Avg Class 2 Price": avg_class_2_price,
    "Avg Class 3 Price": avg_class_3_price
}


print(result)