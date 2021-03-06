import random
import string
import math
import matplotlib.pyplot as plt
local_path = "../CD_TestFiles/"
test_path = "Test Files/"


def string_generator(dictionary, probability, repeat, hist):
    file = open(test_path + "Generator_Output", 'w')
    result = random.choices(dictionary, probability, k=repeat)
    resultSymbols = [i for n, i in enumerate(result) if i not in result[:n]]
    countresults = [0] * len(resultSymbols)
    entropy = 0
    idx = 0
    # Count each occurence of all individual symbols
    for i in resultSymbols:
        countresults[idx] = result.count(i)
        idx += 1
    for i in result:
        file.write(i + ";")
    # Calculate entropy of generated symbols
    for i in countresults:
        prob = i / len(result)
        entropy += prob * math.log(1 / prob, 2)
    file.close()
    if hist:
        plt.bar(list(resultSymbols), countresults, width=0.5)
        plt.show()
    return result, entropy


def pass_gen(min_size, max_size):
    if min_size <= 3:
        print("Min size is 4")
        return
    size = random.randint(min_size, max_size)
    # Possible symbols
    letters = list(string.ascii_letters + string.digits + string.punctuation)
    # Equal probability for each symbol
    probability = [1/len(letters)]*len(letters)
    result = ""
    entropy = 0
    # Generate passwords until requirements are met
    while not check_password(result):
        result, entropy = string_generator(letters, probability, size, False)
    password = ""
    for symbol in result:
        password += symbol
    return password, entropy


def key_gen():
    size = 24
    # Possible symbols
    letters = list(string.ascii_uppercase + string.digits)
    # Equal probability por each symbol
    probability = [1 / len(letters)] * len(letters)
    result = ""
    entropy = 0
    key = ""
    # Generate keys until requirements are met
    while not check_key(result):
        result, entropy = string_generator(letters, probability, size, False)
        key = ""
        idx = 1
        for symbol in result:
            key += symbol
            if idx % 4 == 0 and idx != 24:
                key += "-"
            idx += 1
    return key, entropy


def check_password(text):
    upper = False
    lower = False
    digit = False
    symbol = False
    # Check password conditions
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
    # Check key conditions
    for item in text:
        if string.ascii_uppercase.__contains__(item):
            upper = True
        if upper:
            return True
    return False

def strength(entropy):
    if entropy < 2:
        return "weak"
    elif entropy < 3.5:
        return "medium"
    else:
        return "strong"

# Generate 5 password files and 5 key files
for fileIdx in range(1, 6):
    keyFile = open(test_path + "generated_keys" + str(fileIdx) + ".txt", 'w')
    passFile = open(test_path + "generated_passwords" + str(fileIdx) + ".txt", 'w')
    # Each file has 50 Keys and 50 Passwords
    # Write results and their entropy's to file
    for index in range(0, 50):
        keyword, keyEntropy = key_gen()
        keyFile.write(keyword + " => " + "Entropy: " + str(keyEntropy) + " => Strength: " + strength(keyEntropy) + "\n")
        password00, keyEntropy = pass_gen(12, 24)
        passFile.write(password00 + " => " + "Entropy: " + str(keyEntropy) + " => Strength: " + strength(keyEntropy) + "\n")



# Load test files
fileNames = open("../CD_TestFiles/Nomes.txt")
fileSurnames = open("../CD_TestFiles/Apelidos.txt")
fileLocals = open("../CD_TestFiles/Concelhos.txt")
fileProfessions = open("../CD_TestFiles/Profissoes.txt")
listNames = fileNames.readlines()
listSurnames = fileSurnames.readlines()
listLocals = fileLocals.readlines()
listProfessions = fileProfessions.readlines()

# Remove spaces
for i in range(len(listNames)):
    listNames[i] = listNames[i].strip()
for i in range(len(listSurnames)):
    listSurnames[i] = listSurnames[i].strip()
for i in range(len(listLocals)):
    listLocals[i] = listLocals[i].strip()
for i in range(len(listProfessions)):
    listProfessions[i] = listProfessions[i].strip()

file = open("Test Files/Individuos", 'w')
# Generates 1499 unique IDs
idList = random.sample(range(10000000, 99999999), 1500)
# Generate personal information and attach a unique ID to it
for i in range(1, 1500):
    nNames = random.randint(1, 2)
    name, ignore = string_generator(listNames, [1 / len(listNames)] * len(listNames), nNames, False)
    if nNames == 2: # Exclude names with one FirstName and two surnames
        nNames = random.randint(1, 2)
    surname, ignore = string_generator(listSurnames, [1 / len(listSurnames)] * len(listSurnames), nNames, False)
    residence, ignore = string_generator(listLocals, [1 / len(listLocals)] * len(listLocals), 1, False)
    profession, ignore = string_generator(listProfessions, [1 / len(listProfessions)] * len(listProfessions), 1, False)
    file.write(str(idList[i-1]) + " ;")
    for firstName in name:
        file.write(" " + firstName)
    for lastName in surname:
        file.write(" " + lastName)
    file.write(" ; " + residence[0] + " ; " + profession[0])
    file.write("\n")

# Uses the same ID list as above to generate Bet data
file = open("Test Files/Apostas", 'w')
numbers = [random.sample(range(1, 50), 5) for m in range(1500)]
stars = [random.sample(range(1, 11), 2) for m in range(1500)]
# Generate year and month
# Day is generated depending on year and month
for i in range(1, 1500):
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
