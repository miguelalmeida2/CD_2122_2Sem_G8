import codecs
import string
import math

#USEFUL DATA
ASCSII_SIZE = 255
local_path = "../CD_TestFiles/"
test_path = "../Test_Output/"
CEASER_DISTANCE = 2

#Implementations
def ceaser_cipher(file):
    fileReadDir = local_path + file
    fileRead = codecs.open(fileReadDir, 'r', 'cp1252')
    text = fileRead.read()
    fileWriteDir = test_path + file + "_encoded"
    fileWrite = codecs.open(fileWriteDir, 'w', 'cp1252')
    for i in range(len(text)):
        char = text[i]
        charIndex = ord(char)
        ceaserChar = chr((charIndex + CEASER_DISTANCE) % ASCSII_SIZE)
        fileWrite.write(ceaserChar)
    fileRead.close()
    fileWrite.close()

def ceaser_decipher(file):
    fileReadDir = test_path + file + "_encoded"
    fileRead = codecs.open(fileReadDir, 'r', 'cp1252')
    text = fileRead.read()
    fileWriteDir = test_path + file + "_decoded"
    fileWrite = codecs.open(fileWriteDir, 'w', 'cp1252')
    for i in range(len(text)):
        char = text[i]
        charIndex = ord(char)
        ceaserChar = chr((charIndex - CEASER_DISTANCE) % ASCSII_SIZE)
        fileWrite.write(ceaserChar)
    fileRead.close()
    fileWrite.close()

#Execution
ceaser_cipher("a.txt")
ceaser_decipher("a.txt")
ceaser_cipher("alice29.txt")
ceaser_decipher("alice29.txt")
