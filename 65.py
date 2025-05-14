import math
from fractions import Fraction

with open("dane_ulamki.txt", "r") as file:
    fractions = [tuple(map(int, line.split())) for line in file]

min_fraction = None
for numerator, denominator in fractions:
    value = numerator / denominator
    if min_fraction is None or value < min_fraction[0] or (value == min_fraction[0] and denominator < min_fraction[1][1]):
        min_fraction = (value, (numerator, denominator))

irreducible_count = 0
for numerator, denominator in fractions:
    if math.gcd(numerator, denominator) == 1:
        irreducible_count += 1

sum_numerators = 0
for numerator, denominator in fractions:
    gcd = math.gcd(numerator, denominator)
    reduced_numerator = numerator // gcd
    sum_numerators += reduced_numerator

b = 2**2 * 3**2 * 5**2 * 7**2 * 13
total_fraction = Fraction(0, 1)
for numerator, denominator in fractions:
    total_fraction += Fraction(numerator, denominator)
total_fraction = total_fraction.limit_denominator(b)
numerator_sum = total_fraction.numerator

with open("wyniki_ulamki.txt", "w") as output:
    output.write(f"65.1: {min_fraction[1][0]} {min_fraction[1][1]}\n")
    output.write(f"65.2: {irreducible_count}\n")
    output.write(f"65.3: {sum_numerators}\n")
    output.write(f"65.4: {numerator_sum}\n")
