# #Upg1
# # usd_rate = 11.25
# # eur_rate = 12.45

# # amount_sek = float(input("Ange belopp i SEK: "))

# # amount_usd = amount_sek / usd_rate
# # amount_eur = amount_sek / eur_rate

# # print(f"{amount_sek} SEK i USD är: {amount_usd}")
# # print(f"{amount_sek} SEK i EUR är: {amount_eur}")

# #Upg2
# # ålder = 25
# # is_student = True

# # if ålder < 26 or is_student:
# #     print("Berättigad till studentrabbat!")
# # else:
# #     print("Inte berättigad till studentrabbat!")

# #Upg3
# # fav_movies = ["Star Wars","Star Trek","Inception","The Shawshank Redemption","The Godfather"]

# # for movie in fav_movies:
# #     if "Star" in movie:
# #         print(f"{movie} - Stjärnfilm")
# #     else:
# #         print(movie)
    
# #Upg4
# math_students = {"Anna", "Bertil", "Cecilia", "David", "Emma"}

# science_students = {"Cecilia", "David", "Fredrik", "Greta", "Hanna"}

# both_courses = math_students & science_students
# print(f"Elever som är med i båda kurserna: {both_courses}")

# specific_student = input("Studentnamn: ")

# if specific_student in both_courses:
#     print(f"{specific_student} är med i båda kurserna")
# else:
#     print(f"{specific_student} är inte med i båda kurserna")

# #Upg5
# products = {"mjölk": "25:-", "bröd": "30:-", "kakor": "20:-"}

# search = input("Sök produkt: ")

# if search in products:
#     print(products.pop(search))
# else:
#     print("Produkten finns inte i lager")

# #Upg6
# # import random
# # start_number = 10

# # while start_number >= 0:
# #     print(start_number)
# #     start_number -= random.randint(1, 3)

# #Upg7
# # my_list = ["äpple", "banan", "körsbär", "druva"]

# # bokstav = input("Skriv en bokstav: ")

# # for ord_i_listan in my_list:
# #     if bokstav in ord_i_listan:
# #         print(ord_i_listan)

# #Upg8
# numbers = [10, -5, 20, -15, 30, -25, 50, -40, 60, -35]

# def is_negative(n):
#     return n < 0

# negative_numbers = list(filter(is_negative, numbers))

# print(negative_numbers)

# print(len(negative_numbers))

# #Upg9
# # bok = ("Kingen", "August Löving", 1999)

# # print(f"Boken '{bok[0]}' är skriven av {bok[1]} och publicerades år {bok[2]} ")

# #Upg 10
# # student_points = {"August": 100, "Willy": 90, "Kaan": 45, "Gurra": 80}

# # for name, points in student_points.items():
# #     print(f"{name}: {points} poäng")

# # medelpoäng = sum(student_points.values()) / len(student_points)
# # print(f"Medelpoängen är {medelpoäng:.2f}")


# #Funktion Uppgifter
# #Upg1
# # def hello_world():
# #     print("Hej världen!")

# # hello_world()

# #Upg2
# # def sum(num1, num2):
# #     return num1 + num2

# # resultat = sum(150, 370)

# # print(resultat)

# #Upg3
# # def addera(num1, num2):
# #     return num1 * num2

# # resultat = addera(10, 3)

# # print(resultat)

# #Upg4
# # def tal():
# #     print("42")

# # tal()

# #Upg5
# # def person_info(namn, ålder, stad):
# #     return f"Hej, jag heter {namn}, jag är {ålder} år gammal och bor i {stad}." 

# # personen = person_info("August", 25, "Västerås")

# # print(personen)

# #Upg6
# # def name_age(name, age=33):
# #     return f"Mitt namn är {name} jag är {age} år gammal"

# # person = name_age("August", )

# # print(person)

# #Upg7
# # def omkretsen(radie):
# #     omkrets = 2 * 3.14 * radie
# #     return omkrets

# # cirkel_radie = 100

# # print(omkretsen(cirkel_radie))

# #Upg8
# # def sum_numbers(numbers):
# #     return sum(numbers)

# # test_list = [10, 20, 30, 40, 50]
# # result = sum_numbers(test_list)

# # print(result)

# #Upg9
# # def temp(tempen):
# #     if tempen  < 10:
# #         return "Kallt"
# #     elif tempen > 25:
# #         return "Varm"
# #     else:
# #         return "mild"
    
# # dagens_temp = 11

# # print(temp(dagens_temp))

# #Upg 10
# # def colour():
# #    färg = input("Färg: ")
# #    print(f"Din favorit färg är: {färg}")

# # colour()

# Mer Uppgifter

#Upg1

# valutakurser = {"USD": 0.11, "EUR": 0.095, "GBP": 0.085}

# amount_sek = float(input("Ange ditt belopp i SEK: "))

# for valuta, kurs in valutakurser.items():
#     konverterat_belopp = amount_sek * kurs
#     print(f"{amount_sek} SEK är lika med {konverterat_belopp:.2f} {valuta}")

#Upg2
# def person(ålder, sysselsättning):
#     if ålder <= 19:
#         if sysselsättning == "student":
#             print("Ungdom och student")
#         else:
#             print(f"Ungdom och {sysselsättning}")
#     elif 20 <= ålder <= 64:
#         if sysselsättning == "student":
#             print("Vuxen och student")
#         else:
#          print(f"Vuxen och {sysselsättning}")
#     else:
#         if sysselsättning == "pensionär":
#             print("Pensionär")
#         else:
#             print(f"Pensionär och {sysselsättning}")

# person(18, "Student")
# person(67, "pensionär")
# person(20, "Customer data developer")
# person(17, "Ica medarbetare")

#Upg3
# filmer_och_genrer = {}

# antal_filmer = int(input("Hur många filmer vill du lägga till?: "))

# for _ in range(antal_filmer):
#     titel = input("Ange filmens titel: ")
#     genre = input(f"Ange genren för filmen '{titel}: ")
#     filmer_och_genrer[titel] = genre

# favoritgenre = input("Vad är din favoritgenre?: ")

# for titel, genre in filmer_och_genrer.items():
#     print(f"Film: {titel}, Genre: {genre}")
#     if genre.lower() == favoritgenre.lower():
#         print("Den här filmen är i din favoritgenre")

#Upg4

#Upg5
# produkt_pris_lager = {"mjölk": (15, "i lager"), "bröd": (20, "ej i lager")}

# search = input("Sök produkt: ")

# if search in produkt_pris_lager:
#     pris, hehe = produkt_pris_lager[search]
#     print(pris)
# else:
#     print("Produkten finns ej i lager")


