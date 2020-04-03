# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a, b):
    if a < b:
        t = a
        a = b
        b = t

    a_prime = a % b

    if a_prime == 0:
        return b
    elif a_prime == 1:
        return 1
    
    while a_prime != 0 and a_prime != 1:
        a = b
        b = a_prime
        a_prime = a % b

    if a_prime == 0:
        return b
    elif a_prime == 1:
        return 1
    
if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    #print(gcd_naive(a, b))
    print(gcd(a, b))
