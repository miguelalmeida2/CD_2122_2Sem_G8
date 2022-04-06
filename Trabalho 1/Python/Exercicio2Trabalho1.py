import random
import string
import math
import matplotlib.pyplot as plt


def string_generator(dictionary, probability, repeat, hist):
    file = open("string_output", 'w')
    result = random.choices(dictionary, probability, k=repeat)
    count_results = [0]*len(dictionary)
    idx = 0
    entropy = 0
    for a in dictionary:
        count_results[idx] = result.count(a)
        entropy += probability[idx] * math.log(1 / probability[idx], 2)
        idx += 1
    for b in result:
        file.write(b + ";")
    file.close()
    if hist:
        plt.bar(dictionary, count_results, 0.5)
        plt.show()
    if check_password(result) or check_key(result):
        print("Entropy= " + str(entropy))
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
    print("Password= " + str(password))


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


fileNames = open("../CD_TestFiles/Nomes.txt")
fileSurnames = open("../CD_TestFiles/Apelidos.txt")
fileLocals = open("../CD_TestFiles/Concelhos.txt")
fileProfessions = open("../CD_TestFiles/Profissoes.txt")

listNames = fileNames.readlines()
listSurnames = fileSurnames.readlines()
listLocals = fileLocals.readlines()
listProfessions = fileProfessions.readlines()

for i in range(len(listNames)):
    listNames[i] = listNames[i].strip()
for i in range(len(listSurnames)):
    listSurnames[i] = listSurnames[i].strip()
for i in range(len(listLocals)):
    listLocals[i] = listLocals[i].strip()
for i in range(len(listProfessions)):
    listProfessions[i] = listProfessions[i].strip()

file = open("Output 2C", 'w')
idList = list([0]*1000)
for i in range(0, 1000):
    name = string_generator(listNames, [1 / len(listNames)] * len(listNames), 1, False)
    surname = string_generator(listSurnames, [1 / len(listSurnames)] * len(listSurnames), 1, False)
    residence = string_generator(listLocals, [1 / len(listLocals)] * len(listLocals), 1, False)
    profession = string_generator(listProfessions, [1 / len(listProfessions)] * len(listProfessions), 1, False)
    identification = random.randint(0, 99999999)
    idList[i] = identification
    file.write(str(identification) + " ; " + name[0] + " ; " + surname[0] + " ; " + residence[0] + " ; " + profession[0] + "\n")

file = open("Output 2C2", 'w')
numbers = [[random.randint(1, 50) for n in range(5)] for m in range(1000)]
stars = [[random.randint(1, 11) for n in range(2)] for m in range(1000)]
