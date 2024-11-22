#Upg1
# import matematik_test

# result = matematik_test.addera(10, 5)
# print(result)

# result2 = matematik_test.multiplicera(3, 3)
# print(result2)

#Upg2
# from statistik import medelvarde, median, standardavvikelse

# tal_lista = [10, 20, 30, 40, 50]

# medel = medelvarde(tal_lista)
# print(medel)

# median = median(tal_lista)
# print(median)

# st_avv = standardavvikelse(tal_lista)
# print(st_avv)

#upg3
# import geometriska

# rektangel_area = geometriska.area_r(10, 5)
# print(rektangel_area)

# cirkel_area = geometriska.area_c(7)
# print(cirkel_area)

#upg 4
# from filhantering import skriv_till_fil, las_upp_fil

# filnamn = "exempel.txt"

# skriv_till_fil(filnamn, "Hej! Detta är en testfil.")
# print(f"Innehållet i filen: {las_upp_fil(filnamn)}")

# main.py
from anvandarinmatning import hamta_input

namn = hamta_input("Vad är ditt namn? ")
alder = hamta_input("Hur gammal är du? ")

print(f"Hej {namn}, du är {alder} år gammal.")
