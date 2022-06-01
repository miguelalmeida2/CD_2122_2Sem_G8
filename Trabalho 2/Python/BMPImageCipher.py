# USEFUL DATA
local_path = "../CD_TestFiles/"
test_path = "../Test_Output/"

import cv2
import numpy as np
import math

key = 37


def bmp_cipher(file):
    path = local_path + file
    path_write = test_path + file + "_encoded.bmp"
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # cv2.imshow(file, img)
    # cv2.waitKey()
    # print("Shape of the loaded image is", img.shape)
    rows, cols = img.shape[:2]
    img_output = np.zeros(img.shape, dtype=img.dtype)
    for i in range(rows):
        for j in range(cols):
            img_output[i, j] = img[i ^ key, j ^ key]
    cv2.imwrite(path_write, img_output)
    # cv2.imshow(path_write, img_output)
    # cv2.waitKey()


def bmp_decipher(file):
    path = test_path + file + "_encoded.bmp"
    path_write = test_path + file + "_decoded.bmp"
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # cv2.imshow(file, img)
    # cv2.waitKey()
    # print("Shape of the loaded image is", img.shape)
    rows, cols = img.shape[:2]
    img_output = np.zeros(img.shape, dtype=img.dtype)
    for i in range(rows):
        for j in range(cols):
            img_output[i, j] = img[i ^ key, j ^ key]
    cv2.imwrite(path_write, img_output)
    # cv2.imshow(path_write, img_output)
    # cv2.waitKey()


bmp_cipher("lena.bmp")
bmp_decipher("lena.bmp")
