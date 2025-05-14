from collections import Counter

def read_passwords(file_path):
    """Reads passwords from the given file."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def write_results(file_path, results):
    """Writes results to the given file."""
    with open(file_path, 'w') as file:
        for result in results:
            file.write(result + '\n')

def is_numeric(password):
    """Checks if the password contains only numeric characters."""
    return password.isdigit()

def has_repeated_passwords(passwords):
    """Finds passwords that are repeated and returns them in lexicographical order."""
    counter = Counter(passwords)
    repeated = [password for password, count in counter.items() if count > 1]
    return sorted(repeated)

def has_ascii_sequence(password):
    """Checks if the password contains a fragment of four consecutive ASCII characters."""
    for i in range(len(password) - 3):
        fragment = password[i:i+4]
        if len(set(fragment)) == 4 and all(ord(fragment[j]) + 1 == ord(fragment[j+1]) for j in range(3)):
            return True
    return False

def meets_complexity_requirements(password):
    """Checks if the password meets the complexity requirements."""
    has_digit = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    return has_digit and has_lower and has_upper

def main():
    passwords = read_passwords('hasla.txt')
    results = []

    numeric_passwords_count = sum(1 for password in passwords if is_numeric(password))
    results.append(f"74.1\n{numeric_passwords_count}")

    repeated_passwords = has_repeated_passwords(passwords)
    results.append("74.2")
    results.extend(repeated_passwords)

    ascii_sequence_count = sum(1 for password in passwords if has_ascii_sequence(password))
    results.append(f"74.3\n{ascii_sequence_count}")

    complex_passwords_count = sum(1 for password in passwords if meets_complexity_requirements(password))
    results.append(f"74.4\n{complex_passwords_count}")

    write_results('wyniki_hasla.txt', results)

if __name__ == "__main__":
    main()
