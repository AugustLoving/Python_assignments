# class Car:
#     def __init__(self, make, model, year, color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color

#     def drive(self):
#         print(f"This {self.model} is driving")

#     def stop(self):
#         print(f"This {self.model} is stopped")


# car1 = Car("Volkswagen", "Passat", 2015, "Blue")
# car2 = Car("Ford", "Mustang", 2022, "red")
# print(car2.make)
# print(car2.model)
# print(car2.year)
# print(car2.color)

# car1.drive()
# car2.stop()

# Calculator
# operator = input("Enter an operator (+ 0 * /): ")
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# if operator == "+":
#     result = num1 + num2
#     print(round(result, 3))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result, 3))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result, 3))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result, 3))
# else:
#     print(f"{operator} is invalid operator")

#while loop
# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age cant be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} year old")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")    

# Slot machine
# import random

# def spin_row():
#     symbols = ["🍒", "🍉", "🍋", "🛎️", "💫"]

#     return [random.choice(symbols) for _ in range(3)]
    

# def print_row(row):
#     print("************")
#     print("  ".join(row))
#     print("************")

# def get_payout(row, bet):
#     if row[0] == row[1] == row [2]:
#         if row[0] == "🍒":
#             return bet * 3
#         elif row[0] == "🍉":
#             return bet * 4
#         elif row[0] == "🍋":
#             return bet * 5
#         elif row[0] == "🛎️":
#             return bet * 10
#         elif row[0] == "💫":
#             return bet * 20
#     return 0



# def main():
#     balance = 100

#     print("********************")
#     print("Welcome to IHM slots  ")
#     print("Symbol: 🍒 🍉 🍋 🛎️ 💫")
#     print("************************")

#     while balance > 0:
#         print(f"Current balance {balance} SEK")

#         bet = input("Place your bet amount: ")

#         if not bet.isdigit():
#             print("Please enter a valid number")
#             continue

#         bet = int(bet)

#         if bet > balance:
#             print("Du har inte tillräckligt med cash")
#             continue

#         if bet <= 0:
#             print("bet must be greater than 0")
#             continue

#         balance -= bet

#         row = spin_row()
#         print("Spinning...\n")
#         print_row(row)

#         payout = get_payout(row, bet)

#         if payout > 0:
#             print(f"You won {payout} SEK")
#         else:
#             print("Sorry you lost this round")
        
#         balance += payout

#         play_again = input("Do you want to spin again (Y/N): ").upper()

#         if play_again != "Y":
#             break
#     print("***********************************************")
#     print(f"Game over! Your final balance is {balance} SEK")
#     print("***********************************************")


# if __name__ == "__main__":
#     main()

