# class Student:

#     class_year = 2024
#     num_students = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1


# student1 = Student("Spongebob", 30)
# student2 = Student("Patrick", 35)
# student3 = Student("squidda", 55)
# student4 = Student("Sandy", 27)



# print(f"Tha class of {Student.class_year} has {Student.num_students} students")                                                                                         
# print(student1.name)
# print(student2.name)
# print(student3.name)
# print(student4.name)

# Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
    
#     def eat(self):
#         print(f"{self.name} is eating")
    
#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animal):
#     def speak(self):
#         print(f"Woof!")

# class Cat(Animal):
#     def speak(self):
#         print(f"Meow!")

# class Mouse(Animal):
#     def speak(self):
#         print("Squeek!")

# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mickey")

# cat.speak()

#Multible inheritance
# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Predator, Prey):
#     pass

# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")

# hawk.eat()

#Abstract classes
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
    
#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass


# class Car(Vehicle):

#     def go(self):
#         print("You drive the car")
#     def stop(self):
#         print("You stop the car")

# class Motorcycle(Vehicle):

#     def go(self):
#         print("You ride the motorcycle")


#     def stop(self):
#         print("You stop the motorcycle")


# class Boat(Vehicle):

#     def go(self):
#         print("You sail the booat")

#     def stop(self):
#         print("You anchor the boat")

# boat = Boat()

# boat.go()
# boat.stop()

# super()
# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled

#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius

#     def describe(self):
#         super().describe()
#         print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        

# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width

#     def describe(self):
#         super().describe()
#         print(f"It is a square with an area of {self.width * self.width}cm^2")

# class Triangel(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height

#     def describe(self):
#         super().describe()
#         print(f"It is a triangel with an area of {self.width * self.height / 2}cm^2")

# circle = Circle(color="red", is_filled = True, radius = 5)
# square = Square(color="blue", is_filled = False, width = 6)
# triangel = Triangel(color="yewllow", is_filled = True, width = 7, height = 8)

# circle.describe()

#Polymorphism
from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping
        


shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Skinka", 15)]

for shape in shapes:
    print(f"{shape.area()}cm^2")


