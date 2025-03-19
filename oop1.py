# import random
#
# class Book:
#     def __init__(self, title, author, available=True):
#         self.title = title
#         self.author = author
#         self.available = available
#
#     def __str__(self):
#         return f"'{self.title}' by {self.author}"
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def check_availability(self, title):
#         for book in self.books:
#             if book.title.lower() == title.lower():
#                 status = "Available" if book.available else "Unavailable"
#                 print(f"{book.title} - {status}")
#                 return
#         print(f"Sorry, '{title}' does not exist in the library.")
#
#     def display_book_titles(self):
#         if not self.books:
#             print("No books available in the library.")
#         else:
#             print("Books in the library:")
#             for book in self.books:
#                 print(f"- {book.title}")
#
#
# def get_random_availability():
#     return random.choice([True, False])
#
#
# my_library = Library()
#
# my_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", available=get_random_availability()))
# my_library.add_book(Book("1984", "George Orwell", available=get_random_availability()))
# my_library.add_book(Book("To Kill a Mockingbird", "Harper Lee", available=get_random_availability()))
# my_library.add_book(Book("Pride and Prejudice", "Jane Austen", available=get_random_availability()))
# my_library.add_book(Book("The Catcher in the Rye", "J.D. Salinger", available=get_random_availability()))
# my_library.add_book(Book("Moby-Dick", "Herman Melville", available=get_random_availability()))
# my_library.add_book(Book("War and Peace", "Leo Tolstoy", available=get_random_availability()))
# my_library.add_book(Book("The Hobbit", "J.R.R. Tolkien", available=get_random_availability()))
# my_library.add_book(Book("Brave New World", "Aldous Huxley", available=get_random_availability()))
# my_library.add_book(Book("The Odyssey", "Homer", available=get_random_availability()))
#
#
# my_library.display_book_titles()
#
#
# user_input = input("\nEnter the name of a book to check availability: ")
# my_library.check_availability(user_input)

# class Rectangle:
#     '''this is a rectangle class'''
#     def __init__(self, width=1 , length=5):
#         self.width = width
#         self.length = length
#
#     def get_area(self):
#         return self.width * self.length
#     def get_perimeter(self):
#         return 2 * (self.width + self.length)
#
# obj1 = Rectangle()
# print(obj1.get_area())
# print(obj1.get_perimeter())

# class Car:
#     '''this is a car class'''
#     def __init__(self, model, makeyear, fueltype, color):
#         self.model = model
#         self.makeyear = makeyear
#         self.fueltype = fueltype
#         self.color = color
#
#     def car_sell(self):
#         return "im selling a Mercedes car using gas from 2015"
#
#     def car_buy(self):
#         return "i want to buy a car"

# class Celsius:
#     '''this is a Celsius class'''
#     def __init__(self, temperature):
#         self.__temperature = temperature
#     def __str__(self):
#         return "this is a Temperature class"
#     def get_temp(self):
#         return self.__temperature
#     def set_temp(self, text):
#         self.__temperature

# class Shape:
#     def __init__(self, color):
#         self.color = color
#     def say_hi(self):
#             print(f'I am a shape with {self.color} color')
#
# class Quadrangle(Shape):
#     pass
# class Triangle(Shape):
#     def say_hi(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def say_hi(self):
#         print(f"im a triangle with {self.color} color")
#
#
#
# s1 = Shape("red")
# s1.say_hi()
# q1 = Quadrangle("blue")
# q1.say_hi()
# t1 = Triangle("green")
# t1.say_hi()


class Libraryitem:
    def __init__(self, title, subject, status):
        self.title = title
        self.subject = subject
        self.status = status
    def __str__(self):
        print("i am a library_item class with 3 atributes")

class CD(Libraryitem):
    def __init__(self, title, status):
        self.title = title
        self.status = status
    def __str__(self):
        print("Warning you cannot get CD in the library")


