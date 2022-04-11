import random
import string
import math
import matplotlib.pyplot as plt


def string_generator(dictionary, probability, repeat, hist):
    generator_file = open("Test Files/Generator_Output", 'w')
    result_string = random.choices(dictionary, probability, k=repeat)
    count_results = [0]*len(dictionary)
    idx = 0
    entropy = 0
    for symbol in dictionary:
        count_results[idx] = result_string.count(symbol)
        entropy += probability[idx] * math.log(1 / probability[idx], 2)
        idx += 1
    for symbol in result_string:
        generator_file.write(symbol + ";")
    generator_file.close()
    if hist:
        plt.bar(dictionary, count_results, 0.5)
        plt.show()
    return result_string


def pass_gen(min_size, max_size):
    if min_size <= 3:
        print("Min size is 4")
        return
    size = random.randint(min_size, max_size)
    letters = list(string.ascii_letters + string.digits + string.punctuation)
    probability = [1/len(letters)]*len(letters)
    result = ""
    while not check_password(result):
        result = string_generator(letters, probability, size, False)
    password = ""
    for symbol in result:
        password += symbol
    print("Password= " + str(password))


def key_gen():
    size = 24
    letters = list(string.ascii_uppercase + string.digits)
    probability = [1 / len(letters)] * len(letters)
    result = ""
    while not check_key(result):
        result = string_generator(letters, probability, size, False)
        key = ""
        idx = 1
        for symbol in result:
            key += symbol
            if idx % 4 == 0 and idx != 24:
                key += "-"
            idx += 1
        print("Key= " + key)


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
idList = list([0]*100)
for i in range(1, 100):
    name = string_generator(listNames, [1 / len(listNames)] * len(listNames), random.randint(1, 2), False)
    surname = string_generator(listSurnames, [1 / len(listSurnames)] * len(listSurnames), random.randint(1, 2), False)
    residence = string_generator(listLocals, [1 / len(listLocals)] * len(listLocals), 1, False)
    profession = string_generator(listProfessions, [1 / len(listProfessions)] * len(listProfessions), 1, False)
    idList[i] = i
    file.write(str(i) + " ;")
    for firstName in name:
        file.write(" " + firstName)
    for lastName in surname:
        file.write(" " + lastName )
    file.write(" ; " + residence[0] + " ; " + profession[0])
    file.write("\n")

file = open("Test Files/Apostas", 'w')
numbers = [random.sample(range(1, 50), 5) for m in range(1000)]
stars = [random.sample(range(1, 11), 2) for m in range(1000)]
for i in range(1, 1000):
    year = random.randint(1990, 2020)
    month = random.randint(1, 12)
    if month == 2:
        if year/4 == 0:
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    else:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day = random.randint(1, 31)
        else:
            day = random.randint(1, 30)

    file.write(str(idList[random.randint(0, len(idList))-1]) + " ;")
    num = numbers[random.randint(0, len(numbers))-1]
    file.write(" " + str(num) + " ")
    file.write(":")
    star = stars[random.randint(0, len(stars)-1)]
    file.write(" " + str(star) + " ")
    file.write("; " + str(day) + "-" + str(month) + "-" + str(year) + "\n")
    