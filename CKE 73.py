with open("tekst.txt") as plik:
    tekst = plik.readline()
print(tekst)
slowa = tekst.split()
ile = 0
for slowo in slowa:
    for i in range(len(slowo)-1):
        if slowo[i] == slowo[i+1]:
            ile += 1
            break
print(ile)
slownik = {}
for litera in tekst:
    if litera != " ":
        if litera in slownik:
            slownik[litera] += 1
        else:
            slownik[litera] = 1
print(slownik)
slownik['Z'] = 0
for i in range(26):
    print(chr(i+65),":",slownik[chr(i+65)])

SAMOGLOSKI = {'A', 'E', 'I', 'O', 'U', 'Y'}
najdluzsze = 0  
liczba_slow = 0  
pierwsze_slowo = None  

for slowo in slowa:  
    dlugosc = 0  
    MAX = 0  
    for litera in slowo:  
        if litera not in SAMOGLOSKI:  
            dlugosc += 1  
        else:  
            MAX = max(MAX, dlugosc)  
            dlugosc = 0  
    MAX = max(MAX, dlugosc)  

    if MAX > najdluzsze:  
        najdluzsze = MAX  
        liczba_slow = 1  
        pierwsze_slowo = slowo  
    elif MAX == najdluzsze:  
        liczba_slow += 1  

with open("wyniki.txt", "w") as plik:  
    plik.write(f"73.1: {ile}\n")  

    plik.write("73.2:\n")  
    for i in range(26):  
        litera = chr(i + 65)  
        liczba = slownik.get(litera, 0)  
        plik.write(f"{litera}: {liczba}")  

    plik.write("73.3:\n")  
    plik.write(f"{najdluzsze}\n")  
    plik.write(f"{liczba_slow}\n")  
    plik.write(f"{pierwsze_slowo}\n")  
