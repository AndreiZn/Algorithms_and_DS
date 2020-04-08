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

a = DoublyLinkedList()
a.PushFront(2)
a.PushFront(4)
a.PushBack(10)
a.printDLL()
