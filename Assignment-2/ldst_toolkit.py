# LDST Toolkit - Unit 2 Assignment

# ------------------ Dynamic Array ------------------
class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity

    def append(self, x):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.arr[self.size] = x
        self.size += 1
        print(f"Appended {x} | Size: {self.size}, Capacity: {self.capacity}")

    def _resize(self, new_capacity):
        print(f"Resizing from {self.capacity} to {new_capacity}")
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def pop(self):
        if self.size == 0:
            return "Array is empty"
        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return val

    def __str__(self):
        return str([self.arr[i] for i in range(self.size)])


# ------------------ Singly Linked List ------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_by_value(self, x):
        temp = self.head
        prev = None

        while temp:
            if temp.data == x:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next

    def traverse(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)


# ------------------ Doubly Linked List ------------------
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new_node = DNode(x)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = DNode(x)
                new_node.next = temp.next
                new_node.prev = temp
                if temp.next:
                    temp.next.prev = new_node
                temp.next = new_node
                return
            temp = temp.next

    def delete_at_position(self, pos):
        if not self.head:
            return
        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(pos):
            temp = temp.next
            if not temp:
                return

        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    def traverse(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)


# ------------------ Stack using SLL ------------------
class Stack:
    def __init__(self):
        self.sll = SinglyLinkedList()

    def push(self, x):
        self.sll.insert_at_beginning(x)

    def pop(self):
        if not self.sll.head:
            return "Underflow"
        val = self.sll.head.data
        self.sll.head = self.sll.head.next
        return val

    def peek(self):
        if not self.sll.head:
            return None
        return self.sll.head.data


# ------------------ Queue using SLL ------------------
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return "Underflow"
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        if not self.head:
            return None
        return self.head.data


# ------------------ Parentheses Checker ------------------
def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.peek() == pairs[char]:
                stack.pop()
            else:
                return False

    return stack.peek() is None


# ------------------ MAIN TEST ------------------
if __name__ == "__main__":
    print("\n--- Dynamic Array ---")
    da = DynamicArray()
    for i in range(10):
        da.append(i)

    print("Array:", da)
    print("Pop:", da.pop())
    print("Pop:", da.pop())
    print("Pop:", da.pop())
    print("After Pops:", da)

    print("\n--- Singly Linked List ---")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(3)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(1)
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    sll.traverse()
    sll.delete_by_value(3)
    sll.traverse()

    print("\n--- Doubly Linked List ---")
    dll = DoublyLinkedList()
    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.insert_after(2, 99)
    dll.traverse()
    dll.delete_at_position(1)
    dll.traverse()

    print("\n--- Stack ---")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())

    print("\n--- Queue ---")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    print("Front:", queue.front())
    print("Dequeue:", queue.dequeue())

    print("\n--- Parentheses Checker ---")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(t, "->", is_balanced(t))