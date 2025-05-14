def zadanie_72_1(lines):
    count = 0
    first_pair = None
    for line in lines:
        word1, word2 = line.split()
        if len(word1) >= 3 * len(word2) or len(word2) >= 3 * len(word1):
            count += 1
            if first_pair is None:
                first_pair = (word1, word2)
    return count, first_pair

def zadanie_72_2(lines):
    results = []
    for line in lines:
        word1, word2 = line.split()
        if word2.startswith(word1):
            suffix = word2[len(word1):]
            results.append((word1, word2, suffix))
    return results

def zadanie_72_3(lines):
    max_length = 0
    pairs = []
    for line in lines:
        word1, word2 = line.split()
        common_suffix = ""
        for i in range(1, min(len(word1), len(word2)) + 1):
            if word1[-i:] == word2[-i:]:
                common_suffix = word1[-i:]
            else:
                break
        if len(common_suffix) > max_length:
            max_length = len(common_suffix)
            pairs = [(word1, word2)]
        elif len(common_suffix) == max_length:
            pairs.append((word1, word2))
    return max_length, pairs

def main():
    with open("napisy.txt", "r") as file:
        lines = file.readlines()

    count, first_pair = zadanie_72_1(lines)
    with open("wyniki.txt", "w") as file:
        file.write(f"72.1\nLiczba wierszy: {count}\nPierwsza para: {first_pair}\n\n")

    results = zadanie_72_2(lines)
    with open("wyniki.txt", "a") as file:
        file.write("72.2\n")
        for word1, word2, suffix in results:
            file.write(f"{word1} {word2} -> Dopisane litery: {suffix}\n")
        file.write("\n")

    max_length, pairs = zadanie_72_3(lines)
    with open("wyniki.txt", "a") as file:
        file.write(f"72.3\nMaksymalna długość zakończenia: {max_length}\n")
        for word1, word2 in pairs:
            file.write(f"{word1} {word2}\n")

if __name__ == "__main__":
    main()
