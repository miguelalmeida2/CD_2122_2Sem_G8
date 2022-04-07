import random
import string
import math
import matplotlib.pyplot as plt


class StringEntropyPair:
    # For entropy display
    def __init__(self, text, entropy: int):
        self.text = text
        self.entropy = entropy


def string_generator(dictionary, probability, repeat, hist):
    generator_file = open("Test Files/Generator_Output", 'w')
    result_string = random.choices(dictionary, probability, k=repeat)
    count_results = [0]*len(dictionary)
    idx = 0
    entropy = 0
    for i in dictionary:
        count_results[idx] = result_string.count(i)
        entropy += probability[idx] * math.log(1 / probability[idx], 2)
        idx += 1
    for i in result_string:
        generator_file.write(i + ";")
    generator_file.close()
    if hist:
        plt.bar(dictionary, count_results, 0.5)
        plt.show()
    return StringEntropyPair(result_string, entropy)


def pass_gen(min_size, max_size):
    if min_size <= 3:
        print("Min size is 4")
        return
    size = random.randint(min_size, max_size)
    letters = list(string.ascii_letters + string.digits + string.punctuation)
    probability = [1/len(letters)]*len(letters)
    result = StringEntropyPair("", 0)
    while not check_password(result.text):
        result = string_generator(letters, probability, size, False)
    password = ""
    for i in result.text:
        password += i
    print("Password= " + str(password) + " Entropy= " + str(result.entropy))


def key_gen():
    size = 24
    letters = list(string.ascii_uppercase + string.digits)
    probability = [1 / len(letters)] * len(letters)
    result = StringEntropyPair("", 0)
    while not check_key(result.text):
        result = string_generator(letters, probability, size, False)
        key = ""
        idx = 1
        for d in result.text:
            key += d
            if idx % 4 == 0 and idx != 24:
                key += "-"
            idx += 1
        print("Key= " + key + " Entropy= " + str(result.entropy))


def check_password(text):
    upper = False
    lower = False
    digit = False
    symbol = False
    for item in text:
        if string.ascii_uppercase.__contains__(item):
            upper = True
        if string.ascii_lowercase.__contains__(item):
            lower = True
        if string.digits.__contains__(item):
            digit = True
        if string.punctuation.__contains__(item):
            symbol = True
        if upper and lower and digit and symbol:
            return True
    return False


def check_key(text):
    upper = False
    for item in text:
        if string.ascii_uppercase.__contains__(item):
            upper = True
        if upper:
            return True
    return False


"""
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

file = open("Test Files/Individuos", 'w')
idList = list([0]*1000)
for i in range(0, 1000):
    name = string_generator(listNames, [1 / len(listNames)] * len(listNames), 1, False)
    surname = string_generator(listSurnames, [1 / len(listSurnames)] * len(listSurnames), 1, False)
    residence = string_generator(listLocals, [1 / len(listLocals)] * len(listLocals), 1, False)
    profession = string_generator(listProfessions, [1 / len(listProfessions)] * len(listProfessions), 1, False)
    idList[i] = i
    file.write(str(i) + " ; " + name[0] + " ; " + surname[0] + " ; " + residence[0] + " ; " + profession[0] + "\n")
file = open("Test Files/Apostas", 'w')
numbers = [[random.randint(1, 50) for n in range(5)] for m in range(1000)]
stars = [[random.randint(1, 11) for n in range(2)] for m in range(1000)]
"""