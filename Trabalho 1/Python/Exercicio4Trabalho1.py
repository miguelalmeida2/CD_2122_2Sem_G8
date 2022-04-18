local_path = "../CD_TestFiles/"
test_path = "Test Files/"


def LZ77_Tokenizer(filename: str, window_size: int, buffer_size: int):
    inputText = open(local_path + filename).read()
    outputFile = open(test_path + "TOKENS_" + filename, 'w')
    dictIterator = 0
    labIterator = 0
    while labIterator < len(inputText):
        dictionary = inputText[dictIterator:labIterator]
        lab = inputText[labIterator:labIterator+buffer_size]
        offset, length, char = LZ77_search(dictionary, lab)
        print("(" + str(offset) + ", " + str(length) + ", " + char + ")")
        outputFile.write("(" + str(offset) + ", " + str(length) + ", " + char + ")" + "\n")
        labIterator = labIterator + length + 1
        dictIterator = labIterator - window_size
        if dictIterator < 0:
            dictIterator = 0


def LZ77_search(dictionary, lab):
    dictLength = len(dictionary)
    labLength = len(lab)

    if dictLength == 0:
        return 0, 0, lab[0]

    if labLength == 0:
        return -1, -1, ""

    best_length = 0
    best_offset = 0
    buf = dictionary + lab

    search_pointer = dictLength
    print("search: ", dictionary, " lookahead: ", lab)
    for i in range(0, dictLength):
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

    return best_offset, best_length, buf[search_pointer + best_length]


LZ77_Tokenizer("person.java", 16, 8)
""" 
dict = 
lab = aa
(0, 0, a)
dict = a
lab = ab
(0, 1, b)
dict = aa
lab = bb
(0, 0, b)
dict = aab
lab = ba
(0, 1, a)
dict = aabb
lab = aa
(0, 1, a)
"""
