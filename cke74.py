import time

hasla = []
with open("hasla.txt") as plik:
    for haslo in plik:
        hasla.apppend(haslo.strip())
print(hasla)
licznik1 = 0
for haslo in hasla:
    if haslo.isdigit():
        licznik += 1
print(licznik1)
slownik_hasel = {}
pocz = time.time()
for haslo in hasla:
    if haslo in slownik_hasel:
        slownik_hasel[haslo] += 1
    else:
        slownik_hasel[haslo] = 1
for k, v in slownik_hasel.items():
    if v > 1:
        print(k)
kon = time.time()
print(kon - pocz)
