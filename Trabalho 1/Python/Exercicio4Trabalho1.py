local_path = "../CD_TestFiles/"


def lz77_tokenizer(filename: str, window_size: int, buffer_size: int):
    file = open(local_path + filename)
    dictionary = ""
    lab = file.read(buffer_size)
    while lab != "":
        index, lenght, break_char = find_max_match(dictionary, lab)
        print("("+str(max(0, index))+", "+str(max(0, lenght))+", "+break_char+")")
        dictionary += lab[:lenght+1]
        lab = lab.removeprefix(lab[:lenght+1])
        lab += file.read(lenght+1)
        dictionary = trim_dictionary(dictionary, window_size)
    print(dictionary)


def trim_dictionary(window, max_size):
    while len(window) > max_size:
        window = window.removeprefix(window[0])
    return window


def find_max_match(window, buffer):
    temp_match = buffer[0]
    index = window.find(temp_match)
    idx = 1
    while index >= 0 and len(temp_match) < len(buffer):
        temp_match += buffer[idx]
        index = window.find(temp_match)
        idx += 1
    break_char = temp_match[len(temp_match)-1]
    lenght = len(temp_match)-1
    return window.find(temp_match[:1]), lenght, break_char


outputFile = open("Test Files/a_decompressed.txt", 'w')
lz77_tokenizer("b.txt", 4, 2)
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
(2, 1, a)
dict = aabb
lab = aa
(2, 1, a)

"""
