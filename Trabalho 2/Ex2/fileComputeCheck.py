import string
from crc import CrcCalculator, Crc8
import shutil
import random

# USEFUL DATA
local_path = "../CD_TestFiles/"
test_path = "../Test_Output/"

# Recebe um ficheiro de entrada e produz o respetivo ficheiro de saída
def crc_file_compute(file):
    path = local_path + file
    fin = open(path, 'rb')
    content = bytes(fin.read())
    fin.close()

    crc_calculator = CrcCalculator(Crc8.CCITT, True)
    checksum = hex(crc_calculator.calculate_checksum(content))

    target = test_path + file + "WithCRC"
    shutil.copyfile(path, target)
    
    fout = open(target, 'a')
    fout.write('\n' + checksum)
    fout.close()

    return checksum
    

# Efetua a verificação da integridade do ficheiro, através do cálculo do respetivo síndroma (deteção de erros)
def crc_file_check(file):
    path = test_path + file + "WithCRC"
    fin = open(path, 'r', errors='ignore')
    last_line = fin.readlines()[-1]
    fin.close()

    readCRC = last_line

    checksum = str(crc_file_compute(file))

    return readCRC == checksum
   

testFiles = ["a.txt", "alice29.txt", "cp.htm", "Person.java", "progc.c"]
for file in testFiles:
    crc_file_compute(file)
    if crc_file_check(file):
        print(file, " has no errors\n")
    else: 
        print(file, " has errors\n")


# Apresente resultados experimentais que comprovem o funcionamento das funções desenvolvidas na alínea anterior, para
# as seguintes situações: ausência de bits em erro; percentagem de bits em erro de 0,01 %, 0,1 %, 0,5 %, 1 % e 5 %.
def createError(file, percentage):
    path = test_path + file + "WithCRC"
    target = test_path + file + "WithErrors" + "WithCRC"
    shutil.copyfile(path, target)
    
    fin = open(target, 'rb')
    content = bytearray(fin.read())
    fin.close()

    affectedSize = int(len(content) * (percentage/100))
    print('size = ', len(content), " bytes")
    print("affectedSize = ", affectedSize, " bytes (", percentage, "%)")

    for i in range(affectedSize):
        content[i] = random.randint(0, 255)
    
    fout = open(target, 'wb')
    fout.write(content)
    fout.close()
    shutil.copyfile(target, local_path + file + "withErrors")

errorPercentage = [0, 0.01, 0.1, 0.5, 1, 5]
file = "alice29.txt"

for percentage in errorPercentage:
    createError(file, percentage)
    if crc_file_check(file + "WithErrors"):
        print(file, " has no errors\n")
    else: 
        print(file, " has errors\n")
