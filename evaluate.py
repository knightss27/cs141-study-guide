"""
evaluate.py

Practice problems for on-paper evaluation.

1. 3x Basic Recursion
2. 3x Basic Loops
3. 3x Recursion with Loops

"""

# Basic Recursion

def f1a(n, k):
    """
    Evaluate f1a(5, 3)
    """
    if n == 0:
        return 1

    return f1a(n-1, k) * k

def f1b(n, k):
    """
    Evaluate f1b(6, 3)
    """
    if n == 1:
        return 1

    return f1b(n-1, k) * k

def f1c(n, k):
    """
    Evaluate f1c(7, 3)
    """
    if n < 5:
        if n == 1:
            return 1
        return f1c(n-1, k)

    return f1c(n-2, k) * k

# Basic Loops

def f2a(n, k):
    """
    Evaluate f2a(7, 3)
    """
    c = 0
    for i in range(k):
        c += i

        if i > 5:
            c += n

    return c

def f2b(n, k):
    """
    Evaluate f2b(3, 10)
    """
    s = ""
    for i in range(k):
        s += str(n)

        if i >= k-1:
            s = s.replace("33", "ZP")

    return s

def f2c(n, k):
    """
    Evaluate f2c(3, 5)
    """
    l = [None] * k
    i = 0
    while i < k:
        l[i % 2] = n
        l[i % 2 + 1] = 2
        i += 1

    return l

# Recursion with Loops

def f3a(n, k):
    """
    Evaluate f3a(5, 3)
    """
    for i in range(k):
        if n > 3:
            return f3a(n-1, k)
        return [i] + f3a(n-1, k-1)

    return [n]

def f3b(n, k):
    """
    Evaluate f3b(3, 2)
    """
    if n <= 0:
        return []

    lst = []
    for s in "practice"[0:n]:
        new = str(n) + s
        lst.append(new)

    return lst + f3b(n-1, k)

def f3c(n, k):
    """
    Evaluate f3c(5, 2)
    """
    if k <= 0:
        return "bye."

    s = ""
    for _ in range(k):
        if n % 2 == 1:
            s += "hi," + f3c(n-1, k-1)
        else:
            s += "hey," + f3c(n, k-1)

    return s