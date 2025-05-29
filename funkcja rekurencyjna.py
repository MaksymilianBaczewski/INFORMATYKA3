# def funkcja(n):
#     while n != 0:
#         print(n)
#         n -= 1

# funkcja(10)

def funkcja(n):
    print(n)
    if n == 1:
        return
    funkcja(n-1)

funkcja(10)

def funkcja(n):
    if n < 1:
        return
    funkcja(n-1)
    print(n)

funkcja(10)

def funkcja(n):
    lista = []
    if n < 1:
        return
    lista.append(funkcja(n-1))
    print(lista)

funkcja(20)
