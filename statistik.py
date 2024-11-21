def medelvarde(lista):
    return sum(lista) / len(lista)

def median(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 1:
        return lista[n // 2]
    else:
        mid1 = lista[n // 2 - 1]
        mid2 = lista[n // 2]
        return (mid1 + mid2) / 2
    
def standardavvikelse(lista):
    import statistics
    return statistics.stdev(lista)
