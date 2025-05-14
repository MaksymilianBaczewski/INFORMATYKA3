import itertools
from math import isqrt

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

with open("trojki.txt", "r") as infile, open("wyniki_trojki.txt", "w") as outfile:
    lines = [list(map(int, line.split())) for line in infile]

    outfile.write("66.1\n")
    for triplet in lines:
        if sum_of_digits(triplet[0]) + sum_of_digits(triplet[1]) == triplet[2]:
            outfile.write(f"{triplet}\n")

    outfile.write("66.2\n")
    for triplet in lines:
        a, b, c = triplet
        if is_prime(a) and is_prime(b) and c == a * b:
            outfile.write(f"{triplet}\n")

    outfile.write("66.3\n")
    for line1, line2 in zip(lines, lines[1:]):
        if is_right_triangle(*line1) and is_right_triangle(*line2):
            outfile.write(f"{line1} {line2}\n")

    outfile.write("66.4\n")
    triangle_count = 0
    max_triangle_sequence = 0
    current_sequence = 0

    for triplet in lines:
        if is_triangle(*triplet):
            triangle_count += 1
            current_sequence += 1
            max_triangle_sequence = max(max_triangle_sequence, current_sequence)
        else:
            current_sequence = 0

    outfile.write(f"Total triangle rows: {triangle_count}\n")
    outfile.write(f"Longest triangle sequence: {max_triangle_sequence}\n")
