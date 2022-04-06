def fibonacci(n):
    zero = 0
    first = 1
    print(zero)
    print(first)
    previous = first
    current = first + previous
    for i in range(0, n):
        print(current)
        temp = previous
        previous = current
        current += temp


def progression(n, u, r):
    val = u
    for i in range(0, n):
        print(val)
        val += r


def most_occurrences(file_name):
    table = [0]*128
    file = open(file_name)
    txt = file.read()
    while len(txt) > 0:
        size = len(txt)
        for i in range(0, size):
            char = ord(txt.__getitem__(i))
            table[char] += 1
        txt = file.readline()
    largest = 0
    largestidx = 0
    for i in range(0, len(table)):
        if table[i] >= largest:
            largest = table[i]
            largestidx = i
    print(chr(largestidx))


most_occurrences("Test Files/Test")
fibonacci(25)
progression(10, 10, 5)
