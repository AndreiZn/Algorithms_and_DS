# python3

class Node:
    def __init__(self, key_val=None):
        self.key = key_val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def PushFront(self, key):
        newNode = Node(key)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            head_cur = self.head
            head_cur.prev = newNode
            newNode.next = head_cur
            self.head = newNode

    def TopFront(self):
        if self.head == None:
            return None
        else:
            top_node = self.head
            return top_node.key

    def PopFront(self):
        if self.head == None:
            return
        else:
            sec_top_node = self.head.next
            if sec_top_node == None:
                self.head = None
                self.tail = None
            else:
                sec_top_node.prev = None
                self.head = sec_top_node

    def PushBack(self, key):
        newNode = Node(key)

        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            cur_back = self.tail
            cur_back.next = newNode
            newNode.prev = cur_back
            self.tail = newNode

    def TopBack(self):
        if self.tail == None:
            return None
        else:
            top_back_node = self.tail
            return top_back_node.key

    def PopBack(self):
        if self.head == None:
            return
        else:
            sec_back = self.tail.prev
            if sec_back == None:
                self.head = None
                self.tail = None
            else:
                sec_back.next = None
                self.tail = sec_back

    def Find(self, key):
        if self.head == None:
            return False
        else:
            node = self.head
            while node is not None:
                if node.key == key:
                    return True
                node = node.next
            return False

    def Erase(self, key):
        if self.head == None:
            return
        else:
            node = self.head
            while node is not None:
                if node.key == key:
                    node_prev = node.prev
                    node_next = node.next
                    if node_prev == None:
                        self.PopFront()
                    elif node_next == None:
                        self.PopBack()
                    else:
                        node_prev.next = node_next
                        node_next.prev = node_prev

                node = node.next

    def Empty(self):
        if self.head == None:
            return True
        else:
            return False

    def AddBefore(self, node, key):
        if self.head == None:
            return
        else:
            prev_node = node.prev
            if prev_node == None:
                self.PushFront(key)
            else:
                newNode = Node(key)
                newNode.prev = prev_node
                newNode.next = node
                prev_node.next = newNode
                node.prev = newNode

    def AddAfter(self, node, key):
        if self.head == None:
            return
        else:
            next_node = node.next
            if next_node == None:
                self.PushBack(key)
            else:
                newNode = Node(key)
                newNode.prev = node
                newNode.next = next_node
                node.next = newNode
                next_node.prev = newNode

    def printDLL(self):
        head = self.head
        if head is not None:
            print(head.key)

            el = head.next
            while el is not None:
                print(el.key)
                el = el.next

        else:
            print('Empty DLL')

class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def Enqueueu(self, key):
        self.queue.PushBack(key)

    def ReturnToQueue(self, key):
        self.queue.PushFront(key)

    def Dequeue(self):
        top_front = self.queue.TopFront()
        self.queue.PopFront()
        return top_front

    def GetLast(self):
        return self.queue.TopBack()

    def Empty(self):
        return self.queue.Empty()

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = Queue()
        self.num_elements = 0

    def process(self, request):
        # write your code here
        arrived_at, time_to_process = request.arrived_at, request.time_to_process
        if not self.finish_time.Empty():
            while not self.finish_time.Empty():
                el = self.finish_time.Dequeue()
                self.num_elements -= 1
                if el > arrived_at:
                    self.finish_time.ReturnToQueue(el)
                    self.num_elements += 1
                    break

            if self.size > self.num_elements:
                if self.finish_time.Empty():
                    start_at = arrived_at
                else:
                    start_at = self.finish_time.GetLast()

                self.finish_time.Enqueueu(start_at + time_to_process)
                self.num_elements += 1
                return Response(False, start_at)
            else:
                return Response(True, -1)

        else:
            if self.size > self.num_elements:
                start_at = arrived_at
                self.finish_time.Enqueueu(start_at + time_to_process)
                self.num_elements += 1
                return Response(False, start_at)
            else:
                return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
