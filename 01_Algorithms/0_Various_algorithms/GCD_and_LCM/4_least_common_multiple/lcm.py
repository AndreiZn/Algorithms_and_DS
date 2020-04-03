# Uses python3
import sys

def gcd(a, b):

    if a * b == 0:
        return 0
    
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
    gcdiv = gcd(a,b)
    if a*b == 0:
        print(int(0))
    else:
        print(int(b*a/gcdiv))
