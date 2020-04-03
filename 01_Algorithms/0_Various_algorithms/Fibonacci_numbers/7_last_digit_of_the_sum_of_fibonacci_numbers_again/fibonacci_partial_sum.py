# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum(from_, to):
    if from_ == 0:
        return fibonacci_sum(to)
    else:
        sum = fibonacci_sum(to) - fibonacci_sum(from_ - 1)
        if sum < 0:
            sum = 10 + sum
        return sum

def fibonacci_sum(n):

    p_10 = get_pisano_period(10) # residual (last digit of i-th fib number) repeats with a period of p_10
    fib = []
    
    for j in range(p_10):
        fib.append(calc_fib(j)) # final sum will consist of entries of fib

    s1 = ((n+1) // p_10) * sum(fib)
    s2 = 0
    for i in range((n+1) % p_10):
        #idx = i % 10
        s2 = s2 + fib[i]
        
    return (s1 + s2) % 10
 
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


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    #print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum(from_, to))
    
