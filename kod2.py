def f(x):
    return 2 * x - 1

def wb(x):
    if x > 0:
        return x
    else:
        return -x

def m(a, b, e):
    if f(a) * f(b) >= 0:
        print("f(a) i f(b) muszą mieć przeciwne znaki")
        return None

    while wb(b - a) > e:
        s = (a + b) / 2.0
        if f(s) == 0:
            return s
        elif f(a) * f(s) < 0:
            b = s
        else:
            a = s

    return (a + b) / 2.0

a = -1
b = 4
e = 0.0001
miejsce_zerowe = m(a, b, e)
print(f"Miejsce zerowe funkcji: {miejsce_zerowe}")