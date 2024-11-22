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
# försök = 0

# while True:
#     try:
#         gissning = int(input("Gissa siffran 1-100: "))
#         försök += 1
#     except ValueError:
#         print("Ogilitigt, ange en siffra!")

#     if gissning < random_num:
#         print("För lågt!")
#         continue

#     elif gissning > random_num:
#         print("För högt")
#     else:
#         print(f"Du gissade rätt på {försök} försök, grattis!")
#         break

# 3. Lista ord i bokstavsordning

# mening = input("Skriv en mening: ").lower()

# delad_mening = mening.split()
# delad_mening.sort()
# sorterad_mening = " ".join(delad_mening)

# print(sorterad_mening)

# 4. Enkla statistikberäkningar

# input_list = input("Skriva dina tal, separera med mellanslag: ")
# print(input_list)

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
# fråga_1 = "Vad är huvudstaden i Sverige?"
# fråga_2 = "Vad är 5 + 3?"
# fråga_3 = "Vilket är det största havet på jorden?"


# svars_altenativ_1 = ["Stockholm", "Göteborg", "Västerås"]
# svars_altenativ_2 = ["6", "7", "8"]
# svars_altenativ_3 = ["Atlanten", "Indiska oceanen", "Stilla havet"]


# rätt_svar = {fråga_1: "Stockholm", fråga_2: "8", fråga_3: "Stilla havet"}

# poäng = 0

# def ställ_svar(fråga, altenativ, rätt_svar):
#     print("f\n{fråga}")

# Funktion uppgifter
# 1. Temeratur omvandlare

# def till_celcius(temp, omvandlingstyp):
#     if omvandlingstyp == "c":
#         celsius = (temp - 32) * 5/9
#         print(f"{temp} fahrenheit är {celsius:.2f} grader celcius")
#     elif omvandlingstyp == "f":
#         fahrenheit = (temp * 9/5) + 32
#         print(f"{temp} celcis är {fahrenheit:.2f} grader fahrenheit")
#     else:
#         print("Ogilitigt val, välj C eller F")

# omvandlingstyp = input("Vilken typ vill du omvandla till (C/F): ").lower()
# temp = float(input("Temperatur: "))

# till_celcius(temp, omvandlingstyp)


#2. enkla textanalyser
# def antal_ord(mening):
#     result = mening.split()
#     print(f"Din mening innehåller {len(result)} ord.")
    

# def antal_boks(mening):
#     count = len([char for char in mening if char.isalpha()])
#     print(f"din mening innehåller {count} bokstäver.")

# def längst_ord(mening):
#     longest = max(mening.split(), key=len)
#     print(f"Det längsta ordet är: {longest}")

# mening = input("Skriv en mening: ")

# antal_ord(mening)
# antal_boks(mening)
# längst_ord(mening)

# 3. beräkna area och omkrets av en cirkel
# import math

# radie = float(input("Ange radie: "))

# def ber_area(radie):
#     area = math.pow(radie, 2) * math.pi
#     print(f"Arean är: {area:.2f}")

# def ber_omkrets(radie):
#     omkrets = 2 * radie * math.pi
#     print(f"Omkretsen är: {omkrets:.2f}")


# ber_area(radie)
# ber_omkrets(radie)

# 4. Multiplikationstabell


# def multiplikationstabell(tal, upptill):
#     for i in range(1, upptill + 1):
#         print(f"{tal} X {i} = {tal * i}")

# tal = int(input("Ange ett heltal för multiplikationstabellen: "))
# upptill = int(input("Hur långt ska tabellen gå: "))
    


# multiplikationstabell(tal, upptill)

# 5. Palindrome Checker
# def check_palindrome(text):

#     text = text.replace(" ", "").lower()

#     reverse_text = text[::-1]

#     if reverse_text == text:
#         print("Palindrome!")
#     else:
#         print("Inte Palindrome")
    
# text = input("Ange ett ord eller mening(utan .): ")

# check_palindrome(text)
# import random

# poäng = 100
# kast = 0

# def kasta_tärning():
#     return  random.randint(1, 6)

# while poäng > 50 and poäng < 150:
#     result = kasta_tärning()
#     kast += 1

#     print(f"Tärningens resultat: {result}")

#     if result == 5 or result == 6:
#         poäng += 10
#         print("Du fick 10 poäng!")
#         print(f"Total poäng: {poäng}")
#     else:
#         poäng -= 10
#         print(f"Du förlorade 10 poäng!")
#         print(f"Total poäng: {poäng}")

# if poäng <= 50:
#     print(f"Du förlorade! Antal kast: {kast}")
# elif poäng >= 150:
#     print(f"Du vann! Antal kast: {kast}")

#OOP
# 1. Kunddatabas
