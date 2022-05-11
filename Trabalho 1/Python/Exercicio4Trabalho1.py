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
        # Load dictionary from dictIterator to labIterator
        dictionary = inputText[dictIterator:labIterator]
        # Load look-ahead buffer from labIterator to labIterator+buffer_size
        lab = inputText[labIterator:labIterator+buffer_size]
        # Function returns all data required for a LZ77 token, displayOffset is used to display the correct offset
        offset, length, char, displayOffset = LZ77_search(dictionary, lab)
        # Count each ocurrence of the values in offset and length
        histPosition[displayOffset-1] += 1
        histLength[length] += 1
        #print("(" + str(displayOffset) + ", " + str(length) + ", " + char + ")")
        outputFile.write("(" + str(displayOffset) + ", " + str(length) + ", " + char + ")" + "\n")
        # Move iterator forward
        labIterator = labIterator + length + 1
        # Remove the oldest part of the dictionary
        dictIterator = labIterator - window_size
        # Counting total number of generated tokens
        totalTokens += 1
        # In case dictionary size was smaller than window_size
        # Only relevant while the dictionary is not full
        if dictIterator < 0:
            dictIterator = 0
    # Entropy of Length field of all tokens
    for value in histLength:
        lengthProbablity = value / totalTokens
        if lengthProbablity != 0:
            lengthEntropy += lengthProbablity * math.log(1 / lengthProbablity, 2)
    # Entropy of Offset field of all tokens
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
    # When there is nothing in the dictionary to compare to
    if dictLength == 0:
        return 0, 0, lab[0], 0
    # In case input is invalid
    if labLength == 0:
        return -1, -1, "", -1
    best_length = 0
    best_offset = 0
    displayOffset = 0
    # Sliding window
    buf = dictionary + lab
    # Starts at lab[0]
    search_pointer = dictLength
    for i in range(0, dictLength):
        idx = dictLength
        length = 0
        # While there is a match between dictionary and lab
        while buf[i + length] == buf[search_pointer + length]:
            length = length + 1
            if search_pointer + length == len(buf):
                length = length - 1
                break
            # In case the length surpasses the dictionary
            if i + length >= search_pointer:
                break
        # If current length is better than the previous best_length
        if length > best_length:
            # best_offset will be used to calculate the token's offset
            best_offset = i
            best_length = length
            # displayOffset will be used to correctly display the token's offset
            displayOffset = idx - i
        idx -= 1
    return best_offset, best_length, buf[search_pointer + best_length], displayOffset


testFiles = ["a.txt", "alice29.txt", "cp.htm", "Person.java", "progc.c"]
for file in testFiles:
    LZ77_Tokenizer(file, 16, 4)
