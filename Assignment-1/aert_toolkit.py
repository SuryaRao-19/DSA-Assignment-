# AERT - Algorithmic Efficiency & Recursion Toolkit
# Data Structures Unit 1 Assignment
#Name: Surya Rao
#Roll Number: 2501730243


# -----------------------------
# Stack ADT Implementation
# -----------------------------

class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# -----------------------------
# Factorial (Recursive)
# -----------------------------

def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# -----------------------------
# Fibonacci (Naive Recursion)
# -----------------------------

fib_naive_calls = 0

def fib_naive(n):
    global fib_naive_calls
    fib_naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


# -----------------------------
# Fibonacci (Memoization)
# -----------------------------

fib_memo_calls = 0

def fib_memo(n, memo={}):
    global fib_memo_calls
    fib_memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return n

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


# -----------------------------
# Tower of Hanoi (Recursive)
# -----------------------------

def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        stack.push(move)
        return

    hanoi(n-1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    stack.push(move)

    hanoi(n-1, auxiliary, source, destination, stack)


# -----------------------------
# Recursive Binary Search
# -----------------------------

def binary_search(arr, key, low, high, stack):
    if low > high:
        return -1

    mid = (low + high) // 2
    stack.push(mid)

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1, stack)
    else:
        return binary_search(arr, key, mid + 1, high, stack)


# -----------------------------
# MAIN FUNCTION
# -----------------------------

def main():

    print("----- FACTORIAL TESTS -----")
    factorial_tests = [0,1,5,10]

    for n in factorial_tests:
        print(f"factorial({n}) =", factorial(n))


    print("\n----- FIBONACCI TESTS -----")
    fib_tests = [5,10,20,30]

    for n in fib_tests:

        global fib_naive_calls
        fib_naive_calls = 0
        naive_result = fib_naive(n)

        global fib_memo_calls
        fib_memo_calls = 0
        memo_result = fib_memo(n, {})

        print(f"\nFibonacci n = {n}")
        print("Naive Result:", naive_result)
        print("Naive Calls:", fib_naive_calls)

        print("Memo Result:", memo_result)
        print("Memo Calls:", fib_memo_calls)


    print("\n----- TOWER OF HANOI (N=3) -----")

    stack = StackADT()
    hanoi(3, 'A', 'B', 'C', stack)

    while not stack.is_empty():
        print(stack.pop())


    print("\n----- BINARY SEARCH TESTS -----")

    arr = [1,3,5,7,9,11,13]
    tests = [7,1,13,2]

    for key in tests:
        stack = StackADT()
        result = binary_search(arr, key, 0, len(arr)-1, stack)

        print(f"\nSearch key = {key}")
        print("Index =", result)

        print("Mid indices visited:")
        while not stack.is_empty():
            print(stack.pop())


    print("\nEmpty array test")
    stack = StackADT()
    print(binary_search([], 5, 0, -1, stack))


if __name__ == "__main__":
    main()