import codecs
import EntropyCalculator as Ent
import Histogram as Hist

# USEFUL DATA
ASCII_SIZE = 255
local_path = "../CD_TestFiles/"
test_path = "../Test_Output/"
CAESAR_DISTANCE = 2


# Implementations
def caesar_cipher(file):
    fileReadDir = local_path + file
    fileRead = codecs.open(fileReadDir, 'r', 'cp1252')
    text = fileRead.read()
    fileWriteDir = test_path + file + "_encoded"
    fileWrite = codecs.open(fileWriteDir, 'w', 'cp1252')
    for i in range(len(text)):
        char = text[i]
        charIndex = ord(char)
        ceaserChar = chr((charIndex + CAESAR_DISTANCE) % ASCII_SIZE)
        fileWrite.write(ceaserChar)
    fileRead.close()
    fileWrite.close()


def caesar_decipher(file):
    fileReadDir = test_path + file + "_encoded"
    fileRead = codecs.open(fileReadDir, 'r', 'cp1252')
    text = fileRead.read()
    fileWriteDir = test_path + file + "_decoded"
    fileWrite = codecs.open(fileWriteDir, 'w', 'cp1252')
    for i in range(len(text)):
        char = text[i]
        charIndex = ord(char)
        ceaserChar = chr((charIndex - CAESAR_DISTANCE) % ASCII_SIZE)
        fileWrite.write(ceaserChar)
    fileRead.close()
    fileWrite.close()


key_entropy = 0
# Execution
caesar_cipher("a.txt")
caesar_decipher("a.txt")
plain_entropy = Ent.entropy_calculation(test_path + "a.txt.plain")
Hist.histogram(test_path + "a.txt.plain")
cipher_entropy = Ent.entropy_calculation(test_path + "a.txt_encoded")
Hist.histogram(test_path + "a.txt_encoded")

print("Key Mistake: " + str(key_entropy + plain_entropy - cipher_entropy))
print("Message Mistake: " + str(plain_entropy + key_entropy - cipher_entropy))

caesar_cipher("alice29.txt")
caesar_decipher("alice29.txt")
plain_entropy = Ent.entropy_calculation(test_path + "alice29.txt.plain")
Hist.histogram(test_path + "alice29.txt.plain")
cipher_entropy = Ent.entropy_calculation(test_path + "alice29.txt_encoded")
Hist.histogram(test_path + "alice29.txt_encoded")

print("Key Mistake: " + str(key_entropy + plain_entropy - cipher_entropy))
print("Message Mistake: " + str(plain_entropy + key_entropy - cipher_entropy))
