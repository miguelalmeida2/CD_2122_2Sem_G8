import codecs
import random

test_path = "../CD_TestFiles/"
output_path = "../Test_Output/"


def vernam_cipher(plain_file):
    plain_text = open(plain_file).read()
    plain_text_array = list(plain_text)
    total_char = len(plain_text_array)

    cipher_text_array = list(['0']*total_char)
    key = generate_one_time_key(total_char)

    for idx in range(0, total_char-1):
        cipher_text_array[idx] = chr(ord(plain_text_array[idx]) ^ key[idx])

    return ''.join(cipher_text_array), key


def vernam_decipher(cipher_file, key):
    cipher_text = open(cipher_file).read()
    cipher_text_array = list(cipher_text)
    total_char = len(cipher_text_array)

    plain_text_array = list(['0'] * total_char)

    for idx in range(0, total_char - 1):
        plain_text_array[idx] = chr(ord(cipher_text_array[idx]) ^ key[idx])

    return ''.join(plain_text_array)


def generate_one_time_key(size):
    key = list([0]*size)
    for idx in range(0, size-1):
        key[idx] = random.randint(0, 255)
    return key


cipher, key = vernam_cipher(test_path + "a.txt")
cipher_file = open(output_path + "a.txt.vernam", 'w')
cipher_file.write(cipher)
cipher_file.close()

plain = vernam_decipher(cipher, key)
plain_file = open(output_path + "a.txt.plain", 'w')
plain_file.write(plain)
plain_file.close()
