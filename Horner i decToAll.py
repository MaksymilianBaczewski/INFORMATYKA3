def horner(liczba, system):
    wynik = int(liczba[0])
    for i in range(1, len(liczba)):
        wynik = wynik * system + int(liczba[i])
    return wynik

def decToALL(liczba, system):
    wynik = ""
    while liczba > 0:
        wynik  = str(liczba % system) + wynik
        liczba = liczba//system
    return wynik

print(decToALL(454, 8))
print(horner("11010", 2))
print(horner("301", 4))
print(horner("706", 8))
