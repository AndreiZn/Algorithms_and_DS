#python3
import sys

class StackWithMax():
    def __init__(self):
        self.stack = [None]*400000
        self.p = 0
        self.aux_stack = [None]*400000
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
        else:
            assert(0)

    def Max(self):
        if self.p > 0:
            return self.aux_stack[self.aux_p-1]
        else:
            assert(0)


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
