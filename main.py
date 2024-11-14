# #for-loop
# # for element in sekvens:
#     # Kod att köra för varje element
# names = ["ALice", "Bob", "Charlie"]
# # Iterera genom varje namn i listan
# for name in names:
#     print(name)
# # resultat:
# # Alice
# # Bob
# # Charlie
# for i in range(1, 5):  # range(1, 5) ger 1, 2, 3, 4
#     print(i)

# #while-loop
# # Starta med en räknare
# counter = 1

# # Kör loopen så länge räknaren är mindre än eller lika med 5
# while counter <= 5:
#     print(counter)
#     counter += 1  # Öka räknaren med 1
# # Förväntat resultat:
# # 1
# # 2
# # 3
# # 4
# # 5

# #Uppgifter 4
# #upg1
# num = [1, 2, 3, 4, 5]
# total = 0

# for numbers in num:
#     total += numbers
   
# print(total)

# #upg2
# lista = [3, 12, 7, 21, 5]
# greatest = lista[0]

# for great in lista:
#     if great > greatest:
#         greatest = great
# print(greatest)

# #upg 3
# counter = 1
# while counter <= 10:
#     print(counter)
#     counter += 1

# # upg4
# my_list = [5, 12, 9, 15, 8]
# answer = 0
# i = 0

# while i < len(my_list):
#     if my_list[i] > 10:
#         answer += my_list[i]
#     i += 1

# print(f"svaret på upg 4: {answer}") 

# #upg5
# min_list = [2, 3, 4]
# result = 1

# for numbers in min_list:
#     result *= numbers
    
# print(f"svaret på upg 5: {result}")

# 3 in [1, 2, 3, 4]  # True
# 'p' in "python"  # True

# 5 not in [1, 2, 3, 4]  # True
# 'z' not in "python"  # True

#input
# namn = input("Vad heter du? ")
# print(f"Hej, {namn}!")

# print(round(3.14159))  # 3
# print(round(3.14159, 2)) # 3.14. efter "," hur många decimaler man vill ha

# lista = [1, 2, 3, 4]
# print(sum(lista))  # 10

# lista = [1, 2, 3, 4]
# print(max(lista))  # 4

# lista = [1, 2, 3, 4]
# print(min(lista))  # 1

# lista = [3, 1, 4, 2]
# print(sorted(lista))  # [1, 2, 3, 4]

# printar True om alla elementen är true
# lista = [True, True, True]
# print(all(lista))  # True

# lista = [True, False, True]
# print(all(lista))

# printar true om minst ett element är true
# lista = [False, True, False]
# print(any(lista))  # True

# lista = [False, False, False]
# print(any(lista))  # False

# zip()
# Kombinerar två eller fler iterables och returnerar ett objekt av tupel.
# namn = ["Anna", "Björn", "Carla"]
# ålder = [25, 30, 35]
# for person in zip(namn, ålder):
#     print(person)
# # ('Anna', 25)
# # ('Björn', 30)
# # ('Carla', 35)

# enumerate()
# Lägger till en indexposition till varje element i en iterable.
# lista = ["äpple", "banan", "apelsin"]
# for index, frukt in enumerate(lista):
#     print(index, frukt)
# 0 äpple
# 1 banan
# 2 apelsin

# isinstance()
# Kontrollerar om ett objekt är en instans av en viss klass eller typ.
# x = 5
# print(isinstance(x, int))  # True
# print(isinstance(x, str))  # False

# my_tuple = (1, 2, 2, 3)
# occurrences = my_tuple.count(2)
# print(occurrences)

### Sammanfattning av slicing

# sekvens[start:stop]`**: Från `start` till men inte inklusive `stop`.
# sekvens[start:]`**: Från `start` till slutet.
# sekvens[:stop]`**: Från början till `stop`.
# sekvens[::step]`**: Hela sekvensen med steg `step`.
# sekvens[::-1]`**: Hela sekvensen omvänd.

#UPPGIFTER 5

#Upg 1
# djur = ["hund", "katt", "kanin", "fågel", "orm", "fisk"]

# first_djur = djur[0:3]
# last_djur = djur[3:7]
# mellan_djur = djur[1:5]

# print(first_djur)
# print(last_djur)
# print(mellan_djur)

# #Upg2
# nummer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# varannan_nummer = nummer[::2]
# vartredje_nummer = nummer[::3]

# print(varannan_nummer)
# print(vartredje_nummer)

#Upg 3
# färger = ["röd", "grön", "blå", "gul", "svart"]
# print(färger[::-1])
# py = "python"
# reverse_py = py[::-1]
# print(reverse_py)

#Upg4
# veckodagar = ["måndag", "tisdag", "onsdag", "torsdag", "fredag", "lördag", "söndag"]
# tre_sista_dagarna = veckodagar[-3:]
# print(tre_sista_dagarna)

#Upg5
meddelande = "Välkommen till kursen"

print(meddelande[:9])
print(meddelande[-6:])

