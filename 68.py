from collections import Counter

with open("dane_napisy.txt", "r") as file:
    lines = file.readlines()

result_68_1 = 0
result_68_2 = 0
anagram_groups = {}

for line in lines:
    a, b = line.strip().split()

    if len(set(a)) == 1 and len(set(b)) == 1 and Counter(a) == Counter(b):
        result_68_1 += 1

    if Counter(a) == Counter(b):
        result_68_2 += 1

    sorted_a = ''.join(sorted(a))
    if sorted_a not in anagram_groups:
        anagram_groups[sorted_a] = set()
    anagram_groups[sorted_a].add(a)
    anagram_groups[sorted_a].add(b)

result_68_3 = max(len(group) for group in anagram_groups.values())

with open("wyniki_anagramy.txt", "w") as output_file:
    output_file.write(f"68.1. {result_68_1}\n")
    output_file.write(f"68.2. {result_68_2}\n")
    output_file.write(f"68.3. {result_68_3}\n")
