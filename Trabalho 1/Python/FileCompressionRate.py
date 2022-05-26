import os
import matplotlib.pyplot as plt
local_path = "../CD_TestFiles/"
test_path = "Test Files/"


def compressionRate(file1: str, file2: str):
    file1Size = float(os.stat(file1).st_size)
    file2Size = float(os.stat(file2).st_size)
    plt.bar([file1, file2], [file1Size, file2Size], 0.5)
    plt.show()
    return file2Size / file1Size


testFiles = ["a.txt", "alice29.txt", "cp.htm", "Person.java", "progc.c", "lena.bmp", "Apostas", "Individuos"]
resultFiles = ["a.txt_encoded", "alice29.txt_encoded", "cp.htm_encoded", "Person.java_encoded", "progc.c_encoded",
               "lena.bmp_encoded", "Apostas_encoded", "Individuos_encoded"]
for i in range(0, 8):
    first = local_path + testFiles[i]
    secound = test_path + resultFiles[i]
    print(compressionRate(first, secound))
