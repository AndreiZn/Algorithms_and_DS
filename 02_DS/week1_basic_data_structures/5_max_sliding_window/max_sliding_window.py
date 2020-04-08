# python3


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

class StackWithMax():
    def __init__(self):
        self.stack = [None]*100000
        self.p = 0
        self.aux_stack = [None]*100000
        self.aux_p = 0

    def Push(self, a):
        self.stack[self.p] = a
        self.p += 1
        if self.aux_p == 0:
            self.aux_stack[self.aux_p] = a
            self.aux_p += 1
        elif a>= self.aux_stack[self.aux_p-1]:
            self.aux_stack[self.aux_p] = a
            self.aux_p += 1

    def Pop(self):
        if self.p > 0:
            el = self.stack[self.p-1]
            self.p -= 1
            top_aux = self.aux_stack[self.aux_p-1]
            if el == top_aux:
                self.aux_p -= 1
            return el
        else:
            assert(0)

    def Empty(self):
        if self.p == 0:
            return True
        else:
            return False

    def Max(self):
        if self.p > 0:
            return self.aux_stack[self.aux_p-1]
        else:
            assert(0)

class Queue():
    def __init__(self):
        self.part1 = StackWithMax()
        self.part2 = StackWithMax()

    def Pop(self):
        if not self.part1.Empty():
            self.part1.Pop()
        else:
            while not self.part2.Empty():
                el = self.part2.Pop()
                self.part1.Push(el)
            self.part1.Pop()

    def Push(self, key):
        self.part2.Push(key)

    def Max(self):
        if self.part1.Empty():
            return self.part2.Max()
        elif self.part2.Empty():
            return self.part1.Max()
        else:
            return max(self.part1.Max(), self.part2.Max())

def max_sliding_window(sequence, m):
    maximums = []
    q = Queue()
    for idx in range(m):
        q.Push(sequence[idx])
    maximums.append(q.Max())

    for i in range(m, len(sequence)):
        q.Pop()
        q.Push(sequence[i])
        maximums.append(q.Max())
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    #print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window(input_sequence, window_size))

