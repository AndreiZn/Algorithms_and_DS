# python3

import numpy as np

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences_naive(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def is_prime(num):
    for d in range(2,np.int(np.sqrt(num))+1):
        if num % d == 0:
            return False
    return True

def PolyHash(S, p, x):
    h = 0
    for i in range(len(S)-1, -1, -1):
        h = (h*x + ord(S[i])) % p
    return h

def PrecomputeHashes(T, S_len, p, x):
    H = [0]*(len(T) - S_len + 1)
    # get the symbols from T of len S at the end
    S = T[len(T)-S_len:len(T)]
    H[len(T)-S_len] = PolyHash(S, p, x)
    y = 1
    for i in range(1,S_len+1):
        y = (y*x) % p

    for i in range(len(T) - S_len - 1, -1, -1):
        H[i] = (x*H[i+1] + ord(T[i]) - y*ord(T[i+S_len])) % p

    return H

def get_occurrences(pattern, text):
    p = int(1e15) + 37
    x = 23
    result = []

    # precompute hash for the substring
    pHash = PolyHash(pattern, p, x)
    #print(pHash)
    H = PrecomputeHashes(text, len(pattern), p, x)
    #print(H)
    for i in range(0, len(text) - len(pattern)+1):
        if pHash == H[i]:
            if text[i:i+len(pattern)] == pattern:
                result.append(i)

    return result
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

