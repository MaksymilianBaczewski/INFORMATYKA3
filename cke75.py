3
def szyfruj(wyraz, a, b):
    wynik = ""
    for litera in wyraz:
        n = ord(litera) - 97
        n = n * 5 + 2
        n = n % 26
        wynik = chr(n+97)
    return wynik


def szyfruj(wyraz):
    wynik = ""
    for litera in wyraz:
        n = ord(litera) - 97
        n = n * 5 + 2
        n = n % 26
        wynik = chr(n+97)
    return wynik

with open("tekst.txt") as plik:
    tekst = plik.readline()
wyrazy = tekst.split()
#1
ile = 0 
for wyraz in wyrazy:
    if wyraz[0] == 'd' and wyraz[-1] == 'd':
        ile += 1
        print(wyraz)
print(ile)
# print(ord('z')-97)
# print(chr(97))
# 2
# for wyraz in wyrazy:
#     if len(wyraz) >= 10:
#         print(szyfruj(wyraz))

for wyraz in wyrazy:
    if len(wyraz) >= 10:
        print(szyfruj(wyraz, 5, 2))
with open("probka.txt") as plyk:
    lysta = []
    for linia in plyk:
        lysta = linia.split()
        for a in range(26):
            for b in range(26):
                if lysta[0] == szyfruj(lysta[1], a, b):
                    print(lysta, a, b)
                    break
        for a in range(26):
            for b in range(26):
                if szyfruj[lysta[0], a, b] == lysta[1]:
                    print("szyfrujący:", lysta, a, b)
                    break
