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

# mening = input("Skriv en mening: ").lower()

# delad_mening = mening.split()

# delad_mening.sort()

# print(delad_mening)

# 4. Enkla statistikberäkningar

# input_list = input("Skriva dina tal: ")

# num_list = input_list.split()

# num_list = [float(num) for num in num_list]

# max_num = max(num_list)
# min_num = min(num_list)
# sum_num = sum(num_list)

# print(num_list)
# print(f"Högsta talet är: {max_num}")
# print(f"Lägsta talet är: {min_num}")
# print(f"summan av talen är: {sum_num}")

# 5. Liten frågesport
fråga_1 = "Vad är huvudstaden i Sverige?"
fråga_2 = "Vad är 5 + 3?"
fråga_3 = "Vilket är det största havet på jorden?"


svars_altenativ_1 = ["Stockholm", "Göteborg", "Västerås"]
svars_altenativ_2 = ["6", "7", "8"]
svars_altenativ_3 = ["Atlanten", "Indiska oceanen", "Stilla havet"]


rätt_svar = {fråga_1: "Stockholm", fråga_2: "8", fråga_3: "Stilla havet"}

poäng = 0

def ställ_svar(fråga, altenativ, rätt_svar):
    print("f\n{fråga}")
