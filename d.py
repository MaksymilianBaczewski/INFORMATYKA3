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
