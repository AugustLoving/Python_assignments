# upg 1, 2
# from datetime import datetime

# class Book:
#     def __init__(self, title, author, year, ):
#         self.title = title
#         self.author = author
#         self.year = year
        
#     def get_info(self):
#         return f"Title: '{self.title}', Author: {self.author}, Year: {self.year}"

#     def is_classic(self):
#         current_year = datetime.now().year
#         return current_year - self.year >= 50
        

    
# bok1 = Book("Dark matter", "Blake Crouch", 2016)
# info = bok1.get_info()
# classic = bok1.is_classic()

# print(info)
# print(f"is classic: {classic}")

#upg 3

class Student():
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def average_grade(self):
        average = sum(self.grades) / len(self.grades)
        print(f"genomsnittligt betyg för {self.name}: {average}")
    
student1 = Student("Agge", 25, [100, 90, 95, 92])
student2 = Student("Willy", 27, [80, 77, 90, 95])
student3 = Student("Kaan", 22, [60, 70, 80, 50])

student1.average_grade()
student2.average_grade()
student3.average_grade()
    
#upg 4
# class BankAccount():
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
        
    
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
        
    
#     def get_balance(self):
#         return self.__balance
    

# account = BankAccount()
# account.deposit(100)
# print(account.get_balance())
# account.withdraw(50)
# print(account.get_balance())

# upg 5, 6, 7
# class Animal():
#     def __init__(self, name):
#         self.name = name
    
#     def make_sound(self):
#         return "some sound"
    
#     def describe(self):
#         print(f"This is an animal named {self.name}")

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"
    
#     def describe(self):
#         print(f"This is dog named {self.name}!")

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"

#     def describe(self):
#         print(f"This is cat named {self.name}!")


# def animal_sound(animals):
#     for animal in animals:
#         print(animal.make_sound())




# dog = Dog("Scooby")
# cat = Cat("Garfield")
# djur_laten = [dog, cat]
# animal_sound(djur_laten)
# dog.make_sound()
# cat.make_sound()
# dog.describe()
# cat.describe()

#upg 8
# class Rectangle():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def area(self):
#         area = self.height * self.width
#         print(f"Arean är: {area}cm") 

#     def perimeter(self):
#         omkrets = 2 * (self.height + self.width)
#         print(f"Omkretsen är: {omkrets}cm") 

# rektangel = Rectangle(10, 5)

# rektangel.area()
# rektangel.perimeter()

#upg 9
# class Car():
#     def __init__(self, brand, model, mileage):
#         self.brand = brand
#         self.model = model
#         self.mileage = mileage
    
#     def drive(self, kilometers):
#         self.mileage += kilometers
         

# car1 = Car("Volkswagen", "Passat", 1000)
# car1.drive(50)
# print(car1.mileage)

#upg 10

# class Address():
#     def __init__(self, street, city):
#         self.street = street
#         self.city = city

# class Person():
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

# address = Address("Treklövergatan", "västerås")
# address2 = Address("Dennagata", "Göteborg")
# person1 = Person("August Löving", 24, address)
# person2 = Person("Göta Kanalsson", 50, address2)


# print(person1.name)
# print(person1.age)
# print(person1.address.street)
# print(person1.address.city)

# print(person2.name)
# print(person2.age)
# print(person2.address.street)
# print(person2.address.city)

