# python3


def build_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

def Parent(i):
    return int((i-1)/2)

def LeftChild(i):
    return 2*i + 1

def RightChild(i):
    return 2*i + 2

def Swap (arr, p, m):
    t = arr[p]
    arr[p] = arr[m]
    arr[m] = t
    return arr

def SiftDown(i, data):
    swaps = []
    size = len(data)
    min_idx = i
    l = LeftChild(i)
    if l <= size-1:
        if data[l] < data[min_idx]:
            min_idx = l

    r = RightChild(i)
    if r <= size-1:
        if data[r] < data[min_idx]:
            min_idx = r

    if min_idx != i:
        data = Swap(data, i, min_idx)
        swaps.append((i, min_idx))
        next_swaps = SiftDown(min_idx, data)
        for idx in range(len(next_swaps)):
            swaps.append(next_swaps[idx])
    return swaps

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    size = len(data)
    for i in range(int(size/2)-1, -1, -1):
        #print(i)
        new_swaps = SiftDown(i, data)
        for idx in range(len(new_swaps)):
            swaps.append(new_swaps[idx])
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    #print(swaps)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
