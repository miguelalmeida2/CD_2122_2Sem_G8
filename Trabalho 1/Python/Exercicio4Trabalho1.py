import math
from matplotlib import pyplot as plt
local_path = "../CD_TestFiles/"
test_path = "Test Files/"


def LZ77_Tokenizer(filename: str, window_size: int, buffer_size: int):
    inputText = open(local_path + filename).read()
    outputFile = open(test_path + "TOKENS_" + filename, 'w')
    histPosition = [0]*window_size
    histLength = [0]*buffer_size
    dictIterator = 0
    labIterator = 0
    lengthEntropy = 0
    positionEntropy = 0
    totalTokens: float = 0
    while labIterator < len(inputText):
        dictionary = inputText[dictIterator:labIterator]
        lab = inputText[labIterator:labIterator+buffer_size]
        offset, length, char, displayOffset = LZ77_search(dictionary, lab)
        histPosition[offset] += 1
        histLength[length] += 1
        print("(" + str(displayOffset) + ", " + str(length) + ", " + char + ")")
        outputFile.write("(" + str(displayOffset) + ", " + str(length) + ", " + char + ")" + "\n")
        labIterator = labIterator + length + 1
        dictIterator = labIterator - window_size
        totalTokens += 1
        if dictIterator < 0:
            dictIterator = 0
    for value in histLength:
        lengthProbablity = value / totalTokens
        if lengthProbablity != 0:
            lengthEntropy += lengthProbablity * math.log(1 / lengthProbablity, 2)
    for value in histPosition:
        positionProbablity = value / totalTokens
        if positionProbablity != 0:
            positionEntropy += positionProbablity * math.log(1 / positionProbablity, 2)
    plt.bar(range(0, window_size), histPosition, 0.5)
    plt.show()
    print("Position Entropy:", positionEntropy)
    plt.bar(range(0, buffer_size), histLength, 0.5)
    plt.show()
    print("Length Entropy:", lengthEntropy)


def LZ77_search(dictionary, lab):
    dictLength = len(dictionary)
    labLength = len(lab)
    if dictLength == 0:
        return 0, 0, lab[0], 0
    if labLength == 0:
        return -1, -1, "", -1
    best_length = 0
    best_offset = 0
    displayOffset = 0
    buf = dictionary + lab
    search_pointer = dictLength
    # print("search: ", dictionary, " lookahead: ", lab)
    for i in range(0, dictLength):
        idx = dictLength
        length = 0
        while buf[i + length] == buf[search_pointer + length]:
            length = length + 1
            if search_pointer + length == len(buf):
                length = length - 1
                break
            if i + length >= search_pointer:
                break
        if length > best_length:
            best_offset = i
            best_length = length
            displayOffset = idx - 1
        idx -= 1
    return best_offset, best_length, buf[search_pointer + best_length], displayOffset


testFiles = ["a.txt", "alice29.txt", "cp.htm", "Person.java", "progc.c"]
for file in testFiles:
    LZ77_Tokenizer(file, 16, 4)
