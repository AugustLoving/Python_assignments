#Python Övningar

# 1. Enkel Räknare
# num1 = float(input("Tal ett: "))
# num2 = float(input("Tal två: "))

# operator = input("Vad vill du räkna med? (+ - * /): ")

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
#     if num2 != 0:
#         svar = num1 / num2
#         print(svar) 
#     else:
#         print("Division med noll ej tillåtet!")
# else:
#     print("Invalid operator")

# 2. Gissa talet

# import random

# random_num = random.randint(1, 100)

# while True:
#     try:
#         gissning = int(input("Gissa siffran 1-100: "))
#     except ValueError:
#         print("Ogilitigt, ange en siffra!")

#     if gissning < random_num:
#         print("För lågt!")
#         continue

#     elif gissning > random_num:
#         print("För högt")
#     else:
#         print("Du gissade rätt, grattis!")
#         break

# 3. Lista ord i bokstavsordning

mening = input("Skriv en mening: ").lower()

delad_mening = mening.split()

delad_mening.sort()

print(delad_mening)


