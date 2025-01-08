def horner(liczba, system):
    wynik = int(liczba[0])
    for i in range(1, len(liczba)):
        wynik = wynik * system + int(liczba[i])
    return wynik

ciagi = []
with open("ciagi.txt","r") as plik:
    for linia in plik:
        ciagi.append(linia.strip())
print(ciagi)
licznik = 0
for i in range(len(ciagi)):
    if ciagi[i][:len(ciagi[i]//2)] == ciagi[i][len(ciagi[i])//2]:
        print(ciagi[i])
for i in range(len(ciagi)):
    if "11" not in ciagi[i]:
        licznik += 1
print(licznik)
liczby = []
for i in range(263000):
    liczby.append(1)
for i in range(2,263000):
    if liczby[i] == 1:
        for j in range(i+i, 263000, i):
            liczby[j] = 0
pierwsze = []
for i in range(2,263000):
    if liczby [i] == 1:
        pierwsze.append(i)
print(pierwsze)
for i in range(len(liczby)):
    czynniki = []
    liczba = horner(liczby[i],2)
    liczba2 = liczba
    for j in range(len(pierwsze)):
        while liczba2 % pierwsze[j]:
            liczba2 = liczba2 // pierwsze[j]
            czynniki.append(pierwsze[j])
    if len(czynniki) == 2:
        print(liczba,czynniki)
