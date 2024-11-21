#upg 1
# import math

# tal1 = 64

# kvadratrot = math.sqrt(tal1)

# tal2 = 2

# upphöjt = math.pow(tal2, 8)

# pi = math.pi

# print(kvadratrot)
# print(upphöjt)
# print(pi)


#Upg 2
import random
# rand_num = random.randint(1, 100)

# while rand_num < 50:
#     print(rand_num)
#     rand_num = random.randint(1, 100)
#     print(rand_num)

# print("klart")

#Upg 3
# import datetime

# dagens_datum = datetime.date.today()

# print(dagens_datum)

# tid = datetime.datetime.now()

# print(tid.strftime("%H:%M:%S"))

#Upg 4
# import os

# aktuell_katalog = os.getcwd()
# print(f"Aktuell katalog: {aktuell_katalog}")



# ny_katalog = "testing_katalog"

# if not os.path.exists(ny_katalog):
#     os.mkdir(ny_katalog)
#     print(f"mappen {ny_katalog} skapades!")
# else:
#     print(f"mappen {ny_katalog} finns redan")

# lista_innehåll = os.listdir()
# print("innehåll i nuvarande katalog:")
# for fil in lista_innehåll:
#     print(fil)

#upg 5
import statistics


rand_list = []

while len(rand_list) < 6:
    slump_tal = random.randint(1, 100)
    if slump_tal not in rand_list:
        rand_list.append(slump_tal)
    
medelvärdet = statistics.mean(rand_list)
medianen = statistics.median(rand_list)
standard_avvikelse = statistics.stdev(rand_list)


print(rand_list)
print(f"medelvärdet är: {medelvärdet:.2f}")
print(f"medianen är: {medianen}")
print(f"standardavvikelse: {standard_avvikelse:.2f}")
