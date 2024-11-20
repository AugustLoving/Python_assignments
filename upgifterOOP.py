# upg 1, 2
# from datetime import datetime

# class Book:
#     def __init__(self, title, author, year, ):
#         self.title = title
#         self.author = author
#         self.year = year
        
#     def get_info(self):
#         print(f"Title: '{self.title}', Author: {self.author}, Year: {self.year}")

#     def is_classic(self):
#         current_year = datetime.now().year
#         age = current_year - self.year
#         print(age > 50)
        

    
# bok1 = Book("Dark matter", "Blake Crouch", 2016)

# bok1.get_info()
# bok1.is_classic()

#upg 3
# len / sum: average

# class Student():
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
    
#     def average_grade(self):
#         average = sum(self.grades) / len(self.grades)
#         print(f"genomsnittligt betyg för {self.name}: {average}")
    
# student1 = Student("Agge", 25, [100, 90, 95, 92])
# student2 = Student("Willy", 27, [80, 77, 90, 95])
# student3 = Student("Kaan", 22, [60, 70, 80, 50])

# student1.average_grade()
# student2.average_grade()
# student3.average_grade()
    
#upg 4
class BankAccount():
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        
    
    def get_balance(self):
        return self.__balance
    

account = BankAccount()
account.deposit(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())


