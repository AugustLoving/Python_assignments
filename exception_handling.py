#Upg 1
# try:
#     nummer = float(input("Skriv ett nummer: "))
#     print(f"Du skrev: {nummer}")
# except ValueError:
#     print("Det där var inte ett nummer!")

#Upg 2
# try:
#     täljare = float(input("Skriv en siffra: "))
#     nämnaren = float(input("skriv en siffra: "))
#     result = täljare / nämnaren
#     print(result)
# except ZeroDivisionError:
#     print("Du får inte dela med noll")

#Upg 3
# try:
#     x = float(input("Skriv ett nummer: "))
#     result = 100  / x
# except ValueError:
#     print("Du skrev inte ett giltigt nummer!")

# except ZeroDivisionError:
#     print("Du får inte dela med 0!")

# else:
#     print(result)
# finally:
#     print("Tack för att du använda programmet!")

#Upg 4
# my_list = [1, 2, 3, 4, 5]
# print(my_list)

# try:
#     i = int(input("Sök index: "))
#     print(f"index {i} har '{my_list[i]}' i listan")

# except ValueError:
#     print("Fel: ange ett heltal")
# except IndexError:
#     print("Fel: index utanför listans gränser!")

#upg 5
# min_ordbok =  {"namn": "August", "ålder": 25, "stad": "Västerås"}
# print(min_ordbok)

# try:
#     search = input("Vad vill du söka efter?: ")
#     print(min_ordbok[search])

# except KeyError:
#     print("Fel: Nyckeln finns inte i ordboken")

#Upg 6
# class Vinter:
#     def __init__(self, kyla, snö, jul):
#         self.kyla = kyla
#         self.snö = snö
#         self.jul = jul

#     def tomten(self):
#         pass
#     def rudolf(self):
#         pass

# test1 = Vinter("Kallt!", "Mycket snö", 24)

# try:
#     sök_attribut = input("Sök efter attribut: ")
#     print(getattr(test1, sök_attribut))
# except AttributeError:
#     print("Attributet finns inte")

#Upg 7
# import logging
# import math

# logging.basicConfig(level=logging.ERROR, filename="uppgifterrors.log")

# try:
#     tal = float(input("Skriv ett nummer: "))
#     kvadrat_tal = math.sqrt(tal)
#     print(kvadrat_tal)

# except Exception as error:
#     print(f"ett oväntat fel inträffade: {error}")
#     logging.error(f"Ett fel inträffade: {type(error)} - {error}")

#Upg 8
# try:
#     täljaren = float(input("Skriv täljaren: "))
#     nämnaren = float(input("Skriv nämnaren: "))
#     result = täljaren / nämnaren
    
# except ZeroDivisionError:
#     print("Du kan inte dela med noll!")
# else:
#     print(f"{täljaren} delat med {nämnaren} = {result}")
# finally:
#     print("Tack för att du använde programmet!")

#Upg 9
# import logging
# logging.basicConfig(level=logging.ERROR, filename="uppgifterrors.log")


# try:
#     x = float(input("Skriv ett tal: "))

# except Exception as error:
#     logging.error(f"Ett fel inträffade: {type(error)} - {error}")
#     print("Fel inträffade. Det har loggats till Uppgifterrors.log!")

#Upg 10
# import traceback

# try:
#     tal1 = float(input("Skriv ett tal: "))
#     tal2 = float(input("Skriv ett tal: "))
#     print(f"första talet: {tal1}")
#     print(f"första talet: {tal2}")
# except ValueError:
#     print("Ange ett tal!")
#     traceback.print_exc()

#Uppgifter 2
#Upg 1

# def kontrollera_ålder(age):
#     if age < 0:
#         raise ValueError ("Åldern kan inte vara negativ")
#     else:
#         print(f"Din ålder är {age}")

# try:
#     kontrollera_ålder(-3)
# except ValueError as e:
#     print(F"fel: {e}")

#Upg 2
# def kontrollera_lösenord(lösen):
#     if len(lösen) < 8:
#         raise ValueError ("Lösen är för kort!")
#     elif not any(tecken.isdigit() for tecken in lösen):
#         raise ValueError ("Lösenordet måste innehålla minst en siffra!")
#     print("Lösenordet är godkänt!")
    
# try:
#     kontrollera_lösenord("nilsebbe123")
# except ValueError as e:
#     print(f"Fel: {e}")

#Upg 3
# def kontrollera_lista(lista):
#     if not all(isinstance(element, int) for element in lista):
#         raise TypeError ("Alla element i listan ska vara heltal!")
#     print(sum(lista))

# try:
#     kontrollera_lista([1, "två", 3])
# except TypeError as error:
#     print(f"Fel: {error}")

#Upg 4
# def räkna_bokstäver(sträng):
#     if not sträng:
#         raise ValueError ("Strängen är tom!")
#     print(len(sträng))

# try:
#     räkna_bokstäver("")
# except ValueError as e:
#     print(f"fel: {e}")

#Upg 5
# class OgiltigTemperaturError(Exception):
#     pass

# def kontrollera_temperatur(temp):
#     if temp < -273.15:
#         raise OgiltigTemperaturError("Temperaturen kan inte vara lägre än absoluta nollpunkten!")
#     print(f"Temperaturen är: {temp} grader")

# try:
#     kontrollera_temperatur(-300)
# except OgiltigTemperaturError as e:
#     print(f"fel: {e}")
