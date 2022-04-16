local_path = "../CD_TestFiles/"


def LZ77_Tokenizer(filename: str, window_size: int, buffer_size: int):
    file = open(local_path + filename)
    dictionary = ""
    lab = file.read(buffer_size)
    while lab != "":
        index, lenght, innovation_symbol = LZ77_search(dictionary, lab)
        print("("+str(max(0, index))+", "+str(max(0, lenght))+", "+innovation_symbol+")")
        dictionary += lab[:lenght+1]
        lab = lab.removeprefix(lab[:lenght+1])
        lab += file.read(lenght+1)
        dictionary = trimDictionary(dictionary, window_size)
    print(dictionary)


def trimDictionary(window, max_size):
    while len(window) > max_size:
        window = window.removeprefix(window[0])
    return window


def LZ77_search(search, look_ahead):
    ls = len(search)
    llh = len(look_ahead)

    if ls == 0:
        return 0, 0, look_ahead[0]

    if llh == 0:
        return -1, -1, ""

    best_length = 0
    best_offset = 0
    buf = search + look_ahead

    search_pointer = ls
    print("search: ", search, " lookahead: ", look_ahead)
    for i in range(0, ls):
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


outputFile = open("Test Files/a_decompressed.txt", 'w')
LZ77_Tokenizer("b.txt", 4, 2)
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
