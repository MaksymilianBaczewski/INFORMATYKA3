from math import gcd, isqrt

with open("liczby.txt", "r") as file:
    numbers = list(map(int, file.readlines()))

def zadanie_60_1(numbers):
    smaller_than_1000 = [num for num in numbers if num < 1000]
    count = len(smaller_than_1000)
    last_two = smaller_than_1000[-2:]
    return count, last_two

def count_divisors(n):
    divisors = set()
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

def zadanie_60_2(numbers):
    result = []
    for num in numbers:
        divisors = count_divisors(num)
        if len(divisors) == 18:
            result.append((num, divisors))
    return result

def zadanie_60_3(numbers):
    max_rel_prime = None
    for num in sorted(numbers, reverse=True):
        if all(gcd(num, other) == 1 for other in numbers if num != other):
            max_rel_prime = num
            break
    return max_rel_prime

with open("wyniki.txt", "w") as out:
    count, last_two = zadanie_60_1(numbers)
    out.write(f"60.1\nLiczb mniejszych niż 1000: {count}\nOstatnie dwie: {last_two}\n\n")
    result_60_2 = zadanie_60_2(numbers)
    out.write("60.2\n")
    for num, divisors in result_60_2:
        divisors_str = ", ".join(map(str, divisors))
        out.write(f"Liczba: {num}, Dzielniki: {divisors_str}\n")
    out.write("\n")
    rel_prime = zadanie_60_3(numbers)
    out.write(f"60.3\nNajwiększa liczba względnie pierwsza z innymi: {rel_prime}\n")
