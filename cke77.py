with open("dokad.txt") as plik:
    tekst = plik.readline()
wyrazy = tekst.split()
print(wyrazy)

ile = 0
for wyraz in wyrazy:
