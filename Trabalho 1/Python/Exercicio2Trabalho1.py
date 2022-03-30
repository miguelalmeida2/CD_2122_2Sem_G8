import random
import matplotlib.pyplot as plt
import string


def string_generator(dictionary, probability, repeat, hist):
    file = open("string_output", 'w')
    result = random.choices(dictionary, weights=probability, k=repeat)
    count_results = [0]*len(dictionary)
    idx = 0
    for a in dictionary:
        count_results[idx] = result.count(a)
        idx += 1
    for b in result:
        file.write(b + ";")
    file.close()
    if hist:
        plt.bar(dictionary, count_results, width=0.5)
        plt.show()
    return result


def pass_gen(min_size, max_size):
    if min_size <= 3:
        print("Min size is 4")
        return
    size = random.randint(min_size, max_size)
    letters = list(string.ascii_letters + string.digits + string.punctuation)
    probability = [1/len(letters)]*len(letters)
    result = []
    while not check_password(result):
        result = string_generator(letters, probability, size, False)
    password = ""
    for c in result:
        password += c
    print(password)


def key_gen():
    size = 24
    letters = list(string.ascii_uppercase + string.digits)
    probability = [1 / len(letters)] * len(letters)
    result = []
    while not check_key(result):
        result = string_generator(letters, probability, size, False)
        key = ""
        idx = 1
        for d in result:
            key += d
            if idx % 4 == 0 and idx != 24:
                key += "-"
            idx += 1
        print(key)


def check_password(stuff):
    upper = False
    lower = False
    digit = False
    symbol = False
    for e in stuff:
        if string.ascii_uppercase.__contains__(e):
            upper = True
        if string.ascii_lowercase.__contains__(e):
            lower = True
        if string.digits.__contains__(e):
            digit = True
        if string.punctuation.__contains__(e):
            symbol = True
        if upper and lower and digit and symbol:
            return True
    return False


def check_key(stuff):
    upper = False
    for f in stuff:
        if string.ascii_uppercase.__contains__(f):
            upper = True
        if upper:
            return True
    return False


string_generator(["aaa", "bbb", "ccc", "ddd"], [0.10, 0.20, 0.15, 0.50], 100000, hist=True)
pass_gen(12, 24)
for i in range(0, 30):
    key_gen()
