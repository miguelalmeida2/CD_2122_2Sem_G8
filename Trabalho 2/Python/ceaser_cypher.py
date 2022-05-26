import codecs
import string
import math

#USEFUL DATA
ASCSII_SIZE = 255
local_path = "../CD_TestFiles/"
test_path = "Test_Files/"
CEASER_DISTANCE = 2

#Implementations
def ceaser_cipher(file):
    fileReadDir = local_path + file
    text = codecs.open(file, 'r', 'cp1252').read()
    fileWriteDir = test_path + file + "_encoded"
    fileWrite = codecs.open(fileWriteDir, 'w', 'cp1252')
    for i in range(len(text)):
        char = text[i]
        if char.isdigit():
            int = ord('0') - ord(char)
            ceaserInt = (ord('0') + ((int + CEASER_DISTANCE) % 9))
            fileWrite.write(chr(ceaserInt))
            continue
        if char == ' ' or char == '\n' or char == '\t' or char == '\r\n':
            fileWrite.write(char)
            continue
        charIndex = ord(char)
        ceaserChar = chr((charIndex + CEASER_DISTANCE) % ASCSII_SIZE)
        fileWrite.write(ceaserChar)
    fileWrite.close()

#Execution
ceaser_cipher( "a.txt")
#ceaser_cipher("alice29.txt")
