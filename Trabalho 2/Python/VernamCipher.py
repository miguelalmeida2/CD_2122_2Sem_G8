import random

test_path = "../CD_TestFiles/"
output_path = "../Test_Output/"


def vernam_cipher(plain_file):
    # Automatically gets text encoding
    plain_text = list(open(plain_file).read())
    key = generate_one_time_key(len(plain_text))
    cipher_text = coder(plain_text, key)

    return ''.join(cipher_text), key


def vernam_decipher(cipher_file, key):
    # Uses utf-8 to open encoded file
    cipher_text = list(open(cipher_file, encoding='utf-8').read())
    plain_text = coder(cipher_text, key)

    return ''.join(plain_text)


# Encodes or decodes text using provided key
# Uses Vernam cipher (text XOR key)
def coder(text, key):
    result = list(['0'] * len(key))
    for idx in range(0, len(key)):
        result[idx] = chr(ord(text[idx]) ^ key[idx])
    return result


# Generates a list of 8bit int numbers of specified size
def generate_one_time_key(size):
    key = list([0]*size)
    for idx in range(0, size-1):
        key[idx] = random.randint(0, 255)
    return key


cipher, key = vernam_cipher(test_path + "a.txt")
# Encodes the cipher text in utf-8
cipher = bytes(cipher, 'utf-8')
# Writes utf-8 encoded cipher text to file
output = open(output_path + "a.txt.vernam", 'wb')
output.write(cipher)
output.close()

plain = vernam_decipher(output_path + "a.txt.vernam", key)
# Encodes the plain text in utf-8
plain = bytes(plain, 'utf-8')
# Writes utf-8 encoded plain text to file
output = open(output_path + "a.txt.plain", 'wb')
output.write(plain)
output.close()
