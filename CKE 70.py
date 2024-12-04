from math import sqrt
from scipy.integrate import quad
def f(x):
    return (250 / 3) - (500 / 200) * x - (x ** 2) / 4
def g(x):
    return (30 / 6) - (20 / 3) * x + x ** 2 / 3
def f_prime(x):
    return -500 / 200 - x / 2
def g_prime(x):
    return -20 / 3 + 2 * x / 3

x_min, x_max = 2, 10

P_rect = (x_max - x_min) * (f(x_min) - g(x_min))
area_integral, _ = quad(lambda x: f(x) - g(x), x_min, x_max)
P_remaining = P_rect - area_integral

L_f, _ = quad(lambda x: sqrt(1 + f_prime(x) ** 2), x_min, x_max)
L_g, _ = quad(lambda x: sqrt(1 + g_prime(x) ** 2), x_min, x_max)
Obwód = (x_max - x_min) + abs(f(x_min) - g(x_min)) + L_f + L_g

szerokość_pasa = 0.25
liczba_pasów = int(P_remaining // szerokość_pasa)
długość_pasów = liczba_pasów * (x_max - x_min)

print(f"70.1. Pozostałe pole: {P_remaining:.3f}")
print(f"70.2. Długość taśmy: {int(Obwód + 0.5)}")
print(f"70.3. Suma długości pasów: {int(długość_pasów)}"
