def is_perfect_cube(n):
    return round(n ** (1 / 3)) ** 3 == n

def zadanie_61_1(ciagi):
    count = 0
    max_diff = 0
    for ciag in ciagi:
        diff = ciag[1] - ciag[0]
        for i in range(2, len(ciag)):
            if ciag[i] - ciag[i-1] != diff:
                break
        else:
            count += 1
            if diff > max_diff:
                max_diff = diff
    return count, max_diff

def zadanie_61_2(ciagi):
    result = []
    for ciag in ciagi:
        for liczba in ciag:
            if is_perfect_cube(liczba):
                result.append(liczba)
                break
    return result

def zadanie_61_3(ciagi):
    result = []
    for ciag in ciagi:
        diff = ciag[1] - ciag[0]
        for i in range(2, len(ciag)):
            if ciag[i] - ciag[i-1] != diff:
                result.append(ciag[i])
                break
    return result

ciagi = []
with open("ciagi.txt", "r") as plik:
    while True:
        n = int(plik.readline().strip())
        if not n:
            break
        ciag = list(map(int, plik.readline().split()))
        ciagi.append(ciag)

with open("wynik1.txt", "w") as out:
    count, max_diff = zadanie_61_1(ciagi)
    out.write(f"{count}\n{max_diff}\n")

with open("wynik2.txt", "w") as out:
    result_61_2 = zadanie_61_2(ciagi)
    for res in result_61_2:
        out.write(f"{res}\n")

with open("wynik3.txt", "w") as out:
    result_61_3 = zadanie_61_3(ciagi)
    for res in result_61_3:
        out.write(f"{res}\n")
