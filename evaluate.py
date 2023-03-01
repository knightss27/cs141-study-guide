"""
evaluate.py

Practice problems for on-paper evaluation.

1. 3x Basic Recursion
2. 3x Basic Loops
3. 3x Recursion with Loops

"""

# Basic Recursion

def f1a(n, k):
    if n == 0:
        return 1

    return f1a(n-1, k) * k

# evaluate f1(5, 3)

def f1b(n, k):
    if n == 1:
        return 1

    return f1b(n-1, k) * k

# evaluate f2(6, 3)

def f1c(n, k):
    if n < 5:
        if n == 1:
            return 1
        return f1c(n-1, k)

    return f1c(n-2, k) * k

# evaluate f3(7, 3)

# Basic Loops

def f2a(n, k):
    c = 0
    for i in range(k):
        c += i

        if i > 5:
            c += n

    return c

# evaluate f4(7, 3)

def f2b(n, k):
    s = ""
    for i in range(k):
        s += str(n)

        if i >= k-1:
            s = s.replace("33", "ZP")

    return s

# evaluate f5(3, 6)

def f2c(n, k):
    l = [None] * k
    i = 0
    while i < k:
        l[i % 2] = n
        l[i % 2 + 1] = 2
        i += 1

    return l

# evaluate f6(3, 7)

# Recursion with Loops

def f3a(n, k):
    for i in range(k):
        if n > 3:
            return f3a(n-1, k)
        return [i] + f3a(n-1, k-1)

    return [n]

# evaluate f7(5, 3)

def f3b(n, k):
    if n <= 0:
        return []

    lst = []
    for s in "practice"[0:n]:
        new = str(n) + s
        lst.append(new)

    return lst + f3b(n-1, k)

# evaluate f8(3, 2)

def f3c(n, k):
    if k <= 0:
        return "bye."

    s = ""
    for _ in range(k):
        if n % 2 == 1:
            s += "hi," + f3c(n-1, k-1)
        else:
            s += "hey," + f3c(n, k-1)

    return s

# evaluate f9(5, 2)

print(f3c(5, 2))