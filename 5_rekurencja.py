#1
def sumOdd(n):
    if n <= 0:          
        return 0
    if n % 2 == 1:      
        return n + sumOdd(n - 2)
    else:               
        return sumOdd(n - 1)

#2
def stairs(n):
    if n == 0: 
        return
    stairs(n - 1) 
    print('*' * n) 

#3
def countDigits(n):
    if n < 10:
        return 1
    return 1 + countDigits(n // 10)

#4
def countDownUp(n):
    if n == 0:
        return
    print(n)
    countDownUp(n - 1)
    print(n)

#5
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)
