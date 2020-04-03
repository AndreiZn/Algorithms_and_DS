# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    
    if n <= 1:
        return n
    
    previous_last_dig = 0
    current_last_dig  = 1
    
    for _ in range(n - 1):
        previous_last_dig, current_last_dig = current_last_dig, previous_last_dig + current_last_dig
        current_last_dig = current_last_dig % 10

    return current_last_dig

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
