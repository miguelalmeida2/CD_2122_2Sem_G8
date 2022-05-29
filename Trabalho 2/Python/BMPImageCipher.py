import codecs
import string
import math
import struct
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# USEFUL DATA
local_path = "../CD_TestFiles/"
test_path = "../Test_Output/"


def bmpDecipher(file):
    path = test_path + file
    # taking encryption key as input
    key = 37
    # open file for reading purpose
    fin = open(path, 'rb')
    # storing image data in variable "image"
    image = fin.read()
    fin.close()
    # converting image into byte array to
    # perform encryption easily on numeric data
    image = bytearray(image)
    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ key
    # opening file for writing purpose
    fin = open(path, 'wb')
    # writing encrypted data in image
    fin.write(image)
    fin.close()


def bmpCipher(file):
    path = local_path + file
    # taking encryption key as input
    key = 37
    # open file for reading purpose
    fin = open(path, 'rb')
    # storing image data in variable "image"
    image = fin.read()
    fin.close()
    # converting image into byte array to
    # perform encryption easily on numeric data
    image = bytearray(image)
    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ key
    # opening file for writing purpose
    fin = open(path, 'wb')
    # writing encrypted data in image
    fin.write(image)
    fin.close()


bmpCipher("lena.bmp")
# bmpDecipher("lena.bmp")
