def horner(liczba, system):
    wynik = int(liczba[0])
    for i in range(1, len(liczba)):
        wynik = wynik * system + int(liczba[i])
    return wynik

def decToALL(liczba, system):
    wynik = ""
    while liczba > 0:
        wynik  = str(liczba % system) + wynik
        liczba = liczba // system
    return wynik

def zadanie():
    with open("liczby1.txt", "r") as file1, open("liczby2.txt", "r") as file2:
        liczby1 = [line.strip() for line in file1]
        liczby2 = [int(line.strip()) for line in file2]

    min_liczba_osemkowa = min(liczby1, key=lambda x: horner(x, 8))
    max_liczba_osemkowa = max(liczby1, key=lambda x: horner(x, 8))

    najdluzszy_ciag_start = None
    najdluzszy_ciag_dlugosc = 0

    aktualny_start = liczby2[0]
    aktualna_dlugosc = 1

    for i in range(1, len(liczby2)):
        if liczby2[i] >= liczby2[i - 1]:
            aktualna_dlugosc += 1
        else:
            if aktualna_dlugosc > najdluzszy_ciag_dlugosc:
                najdluzszy_ciag_start = aktualny_start
                najdluzszy_ciag_dlugosc = aktualna_dlugosc
            aktualny_start = liczby2[i]
            aktualna_dlugosc = 1

    if aktualna_dlugosc > najdluzszy_ciag_dlugosc:
        najdluzszy_ciag_start = aktualny_start
        najdluzszy_ciag_dlugosc = aktualna_dlugosc

    liczba_takie_same = 0
    liczba_osemkowe_wieksze = 0

    for ose, dec in zip(liczby1, liczby2):
        ose_dec = horner(ose, 8)
        if ose_dec == dec:
            liczba_takie_same += 1
        elif ose_dec > dec:
            liczba_osemkowe_wieksze += 1

    cyfra_6_dziesietna = sum(str(num).count('6') for num in liczby2)
    cyfra_6_osemkowa = sum(decToALL(num, 8).count('6') for num in liczby2)

    with open("wyniki.txt", "w") as wyniki:
        wyniki.write(f"62.1\n")
        wyniki.write(f"Najmniejsza liczba ósemkowa: {min_liczba_osemkowa}\n")
        wyniki.write(f"Największa liczba ósemkowa: {max_liczba_osemkowa}\n\n")

        wyniki.write(f"62.2\n")
        wyniki.write(f"Pierwszy element najdłuższego niemalejącego ciągu: {najdluzszy_ciag_start}\n")
        wyniki.write(f"Liczba elementów tego ciągu: {najdluzszy_ciag_dlugosc}\n\n")

        wyniki.write(f"62.3\n")
        wyniki.write(f"Liczba wierszy z taką samą wartością: {liczba_takie_same}\n")
        wyniki.write(f"Liczba wierszy, gdzie liczba ósemkowa była większa: {liczba_osemkowe_wieksze}\n\n")

        wyniki.write(f"62.4\n")
        wyniki.write(f"Cyfra 6 w zapisie dziesiętnym: {cyfra_6_dziesietna}\n")
        wyniki.write(f"Cyfra 6 w zapisie ósemkowym: {cyfra_6_osemkowa}\n")

if __name__ == "__main__":
    zadanie()
