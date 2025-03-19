# davaleba1
# while True:
#     try:
#         input1 = int(input("enter the first num: "))
#         input2 = int(input("enter the second num: "))

#         if input2 == 0:
#             print("the second num can not be 0.")
#         else:
#             result = input1 / input2
#             print(result)
#             break

#     except ValueError:
#         print("only numbers are valid for an input.")


# davaleba2
# def devide_nums(num1, num2):
#     try:
#         if num2 == 0:
#             return "num2 can not be 0."

#         result = num1 / num2
#         return result
#     except ValueError:
#         print("there was an error")

# print(devide_nums(10, 2))

# davaleba3
# list1 = [1, 2, 3, 4, 5]
# print(list1[5])
# aq wers index errors (IndexError: list index out of range)
# amis gamosasworeblad una shevcvalot da davprintot iseti index romelic lists aqvs 0-4
# gamosworeba
# list1 = [1, 2, 3, 4, 5]
# print(list1[0] or [1] or [2] or [3] or [4])


#davaleba4
# try:
#     with open("myresult.txt", "r") as file:
#         file.readlines()
#
# except ValueError:
#     print("there is no such file")

#davaleba6
# def check_triangle(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         average = (a + b + c) / 3
#         return average
#     else:
#         raise ValueError("there was an error")
# try:
#     a = int(input("enter a num : "))
#     b = int(input("enter the second num : "))
#     c = int(input("anter the third num : "))
#     print(check_triangle(a, b, c))
#
# except ValueError as ve:
#     print(ve)

#davaleba5
# import math
#
#
# def solve_quadratic(a, b, c):
#     try:
#
#         if a == 0:
#             raise ValueError("Error: a cannot be 0.")
#         discriminant = b ** 2 - 4 * a * c
#         if discriminant == 0:
#             x = -b / (2 * a)
#             return f"One root: {x}"
#
#         elif discriminant > 0:
#             x1 = (-b + math.sqrt(discriminant)) / (2 * a)
#             x2 = (-b - math.sqrt(discriminant)) / (2 * a)
#             return f"Roots: x1 = {x1}, x2 = {x2}"
#
#         else:
#             return "No roots exist."
#     except ValueError as e:
#         return f"Error: {str(e)}"
#     except Exception as e:
#         return f"Error: {str(e)}"
#
# try:
#     a = float(input("Enter 'a' (coefficient of x^2): "))
#     b = float(input("Enter 'b' (coefficient of x): "))
#     c = float(input("Enter 'c' (constant term): "))
#
#     print(solve_quadratic(a, b, c))
#
# except ValueError:
#     print("Error: Please enter valid numbers.")

class Rectangle:
    '''this is Rectangle type'''
    def __init__(self, width, length):
        self.width = width
        self.length = length

obj1 = Rectangle(10, 15)

print(type(obj1))
print(f"obj1's width is {obj1.width}, obj1's length is {obj1.length}")