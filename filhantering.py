def skriv_till_fil(filnamn, text):
    with open(filnamn, 'w') as fil:
        fil.write(text)

def las_upp_fil(filnamn):
    with open(filnamn, 'r') as fil:
        return fil.read()
    
