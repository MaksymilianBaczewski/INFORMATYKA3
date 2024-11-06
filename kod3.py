def f(x):
    return x**2 + 1

a = 0
b = 2
E = 1000
x = (b - a) / E

pole_powierzchni = 0

for i in range(E):
    xi = a + i * x
    yi = f(xi)
    P = x * yi
    pole_powierzchni += P

print(f"Przybliżone pole powierzchni pod wykresem: {pole_powierzchni}")