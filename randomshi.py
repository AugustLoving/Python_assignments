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

# my_list = [1, 2, 3, 4, 5]

# total = 0

# for siffror in my_list:
#     total += siffror

# print(total)

# my_list = [3, 12, 7, 21, 5]
# störst = my_list[0]

# for max_num in my_list:
#     if max_num > störst:
#         störst = max_num

# print(störst)

# counter = 0

# while counter < 10:
#     counter += 1
#     print(counter)

# my_list = [5, 12, 9, 15, 8]

# total = 0

# index = 0

# while index < len(my_list):
#     if my_list[index] > 10:
#         total += my_list[index]
#     index += 1

# print(total)

# my_list = [2, 3, 4]

# result = 1


# for numbers in my_list:
#     result *= numbers
    

# print(result)


# usd_rate = 0.091 
# eur_rate = 0.086

# convert_to = input("Vad vill du konvertera SEK till?(dollar / euro): ").lower()
# amount_sek = float(input("Ange belopp i sek: "))

# if convert_to == "dollar":
#     usd_sek = amount_sek * usd_rate
#     print(f"{amount_sek}KR är ${usd_sek}")
# elif convert_to == "euro":
#     eur_sek = amount_sek * eur_rate
#     print(f"{amount_sek}KR är €{eur_sek}")
# else:
#     print("vänligen ange 'dollar' eller 'euro'")

class Car:
    def __init__(self, brand, modell, year):
        self.brand = brand
        self.modell = modell
        self.year = year

    def is_starting(self):
        print(f"{self.modell} is starting")
    
    def is_stopped(self):
        print(f"{self.modell} is stopped")
        


car1 = Car("VW", "Passat", 2016)
car2 = Car("Porshe", "cayenne", 2022)

car1.is_starting()
car2.is_stopped()