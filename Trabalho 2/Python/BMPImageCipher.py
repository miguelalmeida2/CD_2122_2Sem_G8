# USEFUL DATA
local_path = "../CD_TestFiles/"
test_path = "../Test_Output/"

import cv2
import numpy as np
import math

key = 37


def bmp_cipher(file, x1, y1, x2, y2):
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
            if x1 <= i <= x2 and y1 <= j <= y2:
                img_output[i, j] = img[i ^ key, j ^ key]
            else:
                img_output[i, j] = img[i, j]
    cv2.imwrite(path_write, img_output)

    # cv2.imshow(path_write, img_output)
    # cv2.waitKey()


def bmp_cipherComplete(file):
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


def bmp_decipher(file, x1, y1, x2, y2):
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
            if x1 <= i <= x2 and y1 <= j <= y2:
                img_output[i, j] = img[i ^ key, j ^ key]
            else:
                img_output[i, j] = img[i, j]
    cv2.imwrite(path_write, img_output)
    # cv2.imshow(path_write, img_output)
    # cv2.waitKey()


def bmp_decipherComplete(file):
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


bmp_cipher("lena.bmp", 64, 64, 196, 196)
bmp_decipher("lena.bmp", 64, 64, 196, 196)

bmp_cipherComplete("lena.bmp")
bmp_decipherComplete("lena.bmp")
