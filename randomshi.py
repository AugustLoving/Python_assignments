#password generator
# import random

# random_chars = "qwertyuiopaskdfjg42873459823!!¤%&/)"
# password = ""
# length = input("Hur långt? (5-7): ")

# if length == "5":
#     for new_pass in range(5):
#         password += random.choice(random_chars)
# elif length == "6":
#     for new_pass in range(6):
#         password += random.choice(random_chars)
# elif length == "7":
#     for new_pass in range(7):
#         password += random.choice(random_chars)
# else:
#     print("Invalid input, skriv 5, 6 eller 7")


# print(password)

# operator = input("Hur vill du räkna?(+ - * /): ")
# num1 = float(input("Siffra ett: "))
# num2 = float(input("Siffra två: "))

# if operator == "+":
#     svar = num1 + num2
#     print(svar)
# elif operator == "-":
#     svar = num1 - num2
#     print(svar)
# elif operator == "*":
#     svar = num1 * num2
#     print(svar)
# elif operator == "/":
#     svar = num1 / num2
#     print(svar)
# else: 
#     print("Ogilitig input, (+ - * /)")

# age = 1

# if age >= 18:
#     print("Du är vuxen")
# elif age == 0:
#     print("NOLLA")
# elif age < 18:
#     print("Du är inte vuxen än")

# number =  float(input("nummer: "))

# if number > 0:
#     print("positivt")
# elif number < 0:
#     print("Negativt")
# else:
#     print("Talet är noll")

# age = 25

# if age < 13:
#     print("barn")
# elif 13 <= age <= 19:
#     print("Tonåring")
# else:
#     print("Vuxen")

# my_list = [10, 20, 30, 40]

# my_list[0] = 5
# my_list.append(50)

# # my_list.remove(20) remove(x)
# #pop(index)
# my_list.pop(1)
# print(my_list)

# my_tupl = (1, 2, 3, 4)
# print(my_tupl[2])

# my_dict = {"name": "August", "age": 25, "city": "västerås"}
# my_dict["Country"] = "Sverige"

# print(my_dict)
# print(my_dict.pop("age"))

for i in range(1,5):  # range(1, 5) ger 1, 2, 3, 4
    print(i)