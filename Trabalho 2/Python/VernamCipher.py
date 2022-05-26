import random

test_path = "../CD_TestFiles/"
output_path = "../Test_Output/"


def vernam_cipher(plain_file):
    plain_text = open(plain_file).read()
    plain_text_array = list(plain_text)
    total_char = len(plain_text_array)

    cipher_text_array = list(['0']*total_char)
    key = generate_one_time_key(total_char)

    for idx in range(0, total_char):
        cipher_text_array[idx] = chr(ord(plain_text_array[idx]) ^ key[idx])

    return ''.join(cipher_text_array), key


def vernam_decipher(cipher_file, key):
    cipher_text = open(cipher_file, encoding='utf-8').read()
    cipher_text_array = list(cipher_text)
    total_char = len(cipher_text_array)

    plain_text_array = list(['0'] * total_char)

    for idx in range(0, total_char):
        plain_text_array[idx] = chr(ord(cipher_text_array[idx]) ^ key[idx])

    return ''.join(plain_text_array)


def generate_one_time_key(size):
    key = list([0]*size)
    for idx in range(0, size-1):
        key[idx] = random.randint(0, 255)
    return key


cipher, key = vernam_cipher(test_path + "a.txt")
cipher = bytes(cipher, 'utf-8')
cipher_file = open(output_path + "a.txt.vernam", 'wb')
cipher_file.write(cipher)
cipher_file.close()

plain = vernam_decipher(output_path + "a.txt.vernam", key)
plain = bytes(plain, 'utf-8')
plain_file = open(output_path + "a.txt.plain", 'wb')
plain_file.write(plain)
plain_file.close()
