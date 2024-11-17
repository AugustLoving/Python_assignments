#password generator
import random

random_chars = "qwertyuiopaskdfjg42873459823!!¤%&/)"
password = ""
length = input("Hur långt? (5-7): ")

if length == "5":
    for new_pass in range(5):
        password += random.choice(random_chars)
elif length == "6":
    for new_pass in range(6):
        password += random.choice(random_chars)
elif length == "7":
    for new_pass in range(7):
        password += random.choice(random_chars)
else:
    print("Invalid input, skriv 5, 6 eller 7")


print(password)
