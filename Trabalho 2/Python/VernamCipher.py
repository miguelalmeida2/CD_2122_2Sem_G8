import random
import EntropyCalculator as Ent

test_path = "../CD_TestFiles/"
output_path = "../Test_Output/"


def vernam_cipher(plain_file):
    # Automatically gets text encoding
    with open(plain_file) as plain_reader:
        plain_text = list(plain_reader.read())
    # Generates a unique key
    key = generate_one_time_key(len(plain_text))
    cipher_text = coder(plain_text, key)

    return ''.join(cipher_text), key


def vernam_decipher(cipher_file, key):
    # Uses utf-8 to open encoded file
    with open(cipher_file, encoding='utf-8') as cipher_reader:
        cipher_text = list(cipher_reader.read())
    plain_text = coder(cipher_text, key)

    return ''.join(plain_text)


# Encodes or decodes text using provided key
# Uses Vernam cipher (text XOR key)
def coder(text, key):
    size = len(key)
    result = list(['0'] * size)
    for idx in range(0, size):
        result[idx] = chr(ord(text[idx]) ^ key[idx])
    return result


# Generates a list of 8bit int numbers of specified size
def generate_one_time_key(size):
    key = list([0]*size)
    for idx in range(0, size-1):
        key[idx] = random.randint(0, 255)
    return key


# ------------------------------ Test with a.txt ------------------------------

cipher, key = vernam_cipher(test_path + "a.txt")
# Encodes the cipher text in utf-8
cipher = bytes(cipher, 'utf-8')
# Writes utf-8 encoded cipher text to file
with open(output_path + "a.txt.vernam", 'wb') as output:
    output.write(cipher)

plain = vernam_decipher(output_path + "a.txt.vernam", key)
# Encodes the plain text in utf-8
plain = bytes(plain, 'utf-8')
# Writes utf-8 encoded plain text to file
with open(output_path + "a.txt.plain", 'wb') as output:
    output.write(plain)

Ent.entropy(output_path + "a.txt.vernam")
Ent.entropy(output_path + "a.txt.plain")

# ------------------------------ Test with alice29.txt ------------------------------

# For some reason some bytes get lost when writing then reading large files.
# Retry encoding and decoding process until successful.
while True:
    try:
        cipher, key = vernam_cipher(test_path + "alice29.txt")
        # Encodes the cipher text in utf-8
        cipher = bytes(cipher, 'utf-8')
        # Writes utf-8 encoded cipher text to file
        with open(output_path + "alice29.txt.vernam", 'wb') as output:
            output.write(cipher)

        plain = vernam_decipher(output_path + "alice29.txt.vernam", key)
        # Encodes the plain text in utf-8
        plain = bytes(plain, 'utf-8')
        # Writes utf-8 encoded plain text to file
        with open(output_path + "alice29.txt.plain", 'wb') as output:
            output.write(plain)

    except IndexError:
        pass
    else:
        Ent.entropy(output_path + "alice29.txt.vernam")
        Ent.entropy(output_path + "alice29.txt.plain")
        break
