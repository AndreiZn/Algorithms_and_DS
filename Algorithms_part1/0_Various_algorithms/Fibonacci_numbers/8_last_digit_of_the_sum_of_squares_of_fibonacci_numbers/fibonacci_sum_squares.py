# Uses python3
from sys import stdin

def calc_fib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    f = [0]*(n+1)
    f[0] = 0
    f[1] = 1


    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
        
    return f[n]

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def get_pisano_period(m):

    a = [0]
    a.append(1)
    i, last, cur = 2, 0, 1

    while cur != 0 or last != 1:
        a.append((a[i-1] + a[i-2]) % m)
        cur = a[i]
        last = a[i-1]
        i = i + 1
    return i - 1

def get_fhuge(n,m):

    p = get_pisano_period(m)

    r = n % p

    return calc_fib(r) % m

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

# represent the sum of squares of fibonacci numbers as an area of a rectangle with
# horizontal side = F_n + F_n-1; vertical side = F_n-1 + F_n-2 
def fibonacci_sum_squares(n):
    h = get_fhuge(n+1,10)
    v = get_fhuge(n,10)
    s = h*v
    return h*v % 10

if __name__ == '__main__':
    n = int(stdin.read())
    #print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares(n))
