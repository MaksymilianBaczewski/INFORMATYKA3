import os

with open("szyfr1.txt") as plik:
    linie = plik.readlines()
    napisy = [linie[i].strip() for i in range(6)]
    klucz = list(map(int, linie[6].strip().split()))

# 76.1
def szyfruj_przestawieniowo(napis, klucz):
    napis = list(napis) 
    n = len(klucz)
    
    for i in range(n):
        j = klucz[i] - 1
        napis[i], napis[j] = napis[j], napis[i]
    
    return "".join(napis)

zaszyfrowane_napisy = [szyfruj_przestawieniowo(napis, klucz) for napis in napisy]

with open("wyniki_szyfr1.txt", "w") as plik_wynikowy:
    for zaszyfrowany in zaszyfrowane_napisy:
        plik_wynikowy.write(zaszyfrowany + "\n")

# 76.2
with open("szyfr2.txt") as plik:
    linie = plik.readlines()
    napis = linie[0].strip()
    klucz = list(map(int, linie[1].strip().split()))

def deszyfruj_przestawieniowo(napis, klucz):
    napis = list(napis)
    n = len(klucz)
    odwrotny_klucz = [0] * n
    
    for i in range(n):
        odwrotny_klucz[klucz[i] - 1] = i + 1
    
    for i in range(n):
        j = odwrotny_klucz[i] - 1
        napis[i], napis[j] = napis[j], napis[i]
    
    return "".join(napis)

zaszyfrowany_napis = szyfruj_przestawieniowo(napis, klucz)

with open("wyniki_szyfr2.txt", "w") as plik_wynikowy:
    plik_wynikowy.write(zaszyfrowany_napis + "\n")

# 76.3
with open("szyfr3.txt") as plik:
    zaszyfrowany_napis = plik.readline().strip()
    klucz = [6, 2, 4, 1, 5, 3]

def test_szyfrowania(napis, klucz):
    zaszyfrowany = szyfruj_przestawieniowo(napis, klucz)
    odszyfrowany = deszyfruj_przestawieniowo(zaszyfrowany, klucz)
    return napis == odszyfrowany


odszyfrowany_napis = deszyfruj_przestawieniowo(zaszyfrowany_napis, klucz)

with open("wyniki_szyfr3.txt", "w") as plik_wynikowy:
    plik_wynikowy.write(odszyfrowany_napis + "\n")
