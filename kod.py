P = int(input("Podaj liczbę do obliczenia pierwiastka: "))
a1 = 1
a2 = P
E = 0.01

def f(x):
    return 2 * x - 1

def wb(x):
    if x > 0:
        return x
    else:
        return -x

while wb(a1 - a2) > E:
    a1 = (a1 + a2) / 2
    a2 = P / a1
print(f"Pierwiastek liczby {P} wynosi około: {a1}")