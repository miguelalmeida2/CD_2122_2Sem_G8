import random
import matplotlib.pyplot as plt
import string

def stringsource(dictionary, probability, repeat, hist):
    file = open("stringoutput", 'w')
    result = random.choices(dictionary, weights=probability, k=repeat)
    countresults = [0]*len(dictionary)
    idx = 0
    for i in dictionary:
        countresults[idx] = result.count(i)
        idx += 1
    for i in result:
        file.write(i + ";")
    file.close()
    if(hist):
        plt.bar(dictionary, countresults, width=0.5)
        plt.show()
    return result

def passGen(min, max):
    if min <= 3:
        print("Min size is 4")
        return
    size = random.randint(min, max)
    letters = list(string.ascii_letters + string.digits + string.punctuation)
    probability = [1/len(letters)]*len(letters)
    result = []
    while not checkPassword(result):
        result = stringsource(letters, probability, size, False)
    password = ""
    for i in result:
        password += i
    print(password)

def keyGen():
    size = 24
    letters = list(string.ascii_uppercase + string.digits)
    probability = [1 / len(letters)] * len(letters)
    result = []
    while not checkKey(result):
        result = stringsource(letters, probability, size, False)
        key = ""
        idx = 1
        for i in result:
            key += i
            if idx % 4 == 0 and idx != 24:
                key += "-"
            idx += 1
        print(key)


def checkPassword(stuff):
    upper = False
    lower = False
    digit = False
    symbol = False
    for i in stuff:
        if string.ascii_uppercase.__contains__(i):
            upper = True
        if string.ascii_lowercase.__contains__(i):
            lower = True
        if string.digits.__contains__(i):
            digit = True
        if string.punctuation.__contains__(i):
            symbol = True
        if upper and lower and digit and symbol:
            return True
    return False

def checkKey(stuff):
    upper = False
    for i in stuff:
        if string.ascii_uppercase.__contains__(i):
            upper = True
        if upper:
            return True
    return False


stringsource(["aaa", "bbb", "ccc", "ddd"], [0.10, 0.20, 0.15, 0.50], 100000, hist=True)
passGen(12, 24)
for i in range(0, 30):
    keyGen()


