from codecs import ignore_errors
from crc import CrcCalculator, Crc8
import shutil
import random

# USEFUL DATA
local_path = "../CD_TestFiles/"
test_path = "../Test_Output/"

# a)
# Recebe um ficheiro de entrada e produz o respetivo ficheiro de saída
def crc_file_compute(fileName):
    inputPath = local_path + fileName
    fin = open(inputPath, 'rb')
    content = bytes(fin.read())
    fin.close()

    crc_calculator = CrcCalculator(Crc8.CCITT, True)
    checksum = hex(crc_calculator.calculate_checksum(content))

    outputPath = test_path + fileName.split(".")[0] + "WithCRC." + fileName.split(".")[1]

    shutil.copyfile(inputPath, outputPath)
    
    fout = open(outputPath, 'a')
    fout.write('\n' + checksum)
    fout.close()

    return checksum
    

# Efetua a verificação da integridade do ficheiro, através do cálculo do respetivo síndroma (deteção de erros)
def crc_file_check(fileName):
    inputPath = test_path + fileName.split(".")[0] + "WithCRC." + fileName.split(".")[1]

    fin = open(inputPath, 'r', errors='ignore')
    last_line = fin.readlines()[-1]
    fin.close()

    checksum = str(crc_file_compute(fileName))

    print("read : (" + last_line + ") from " + inputPath)
    print("calculated : (" + checksum + ") from " + fileName)
    return last_line == checksum

testFiles = ["alice29.txt", "cp.htm", "Person.java", "progc.c", "a.txt"]

for fileName in testFiles:
    crc_file_compute(fileName)
    
    if crc_file_check(fileName):
        print(fileName, "-> No errors\n")
    else: 
        print(fileName, "-> Error detected\n")
      
def deleteLastLine(path):
    fd = open(path, "r", errors='ignore')
    d = fd.read()
    fd.close()
    m = d.split("\n")
    s = "\n".join(m[:-1])
    fd = open(path, "w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()

# b) Apresente resultados experimentais que comprovem o funcionamento das funções desenvolvidas na alínea anterior, para
# as seguintes situações: ausência de bits em erro; percentagem de bits em erro de 0,01 %, 0,1 %, 0,5 %, 1 % e 5 %.

# Função geradora de erros num ficheiro, de acordo com uma percentagem afetada passada como parâmetro
def createError(fileName, percentage):
    inputPath = test_path + fileName.split(".")[0] + "WithCRC." + fileName.split(".")[1]
    errorOutputPath = local_path + fileName.split(".")[0] + "WithErrors." + fileName.split(".")[1]
    errorCRCOutputPath = test_path + fileName.split(".")[0] + "WithErrorsWithCRC." + fileName.split(".")[1]
    shutil.copyfile(inputPath, errorCRCOutputPath)
    
    fin = open(errorCRCOutputPath, 'rb')
    content = bytearray(fin.read())
    fin.close()

    affectedSize = int(len(content) * (percentage/100))
    print('size = ', len(content), " bytes")
    print("affectedSize = ", affectedSize, " bytes (", percentage, "%)")

    for i in range(affectedSize):
        content[i] = random.randint(0, 255)
    
    fout = open(errorCRCOutputPath, 'wb')
    fout.write(content)
    fout.close()
    
    shutil.copyfile(errorCRCOutputPath, errorOutputPath)
    deleteLastLine(errorOutputPath)

errorPercentage = [0, 0.01, 0.1, 0.5, 1, 5]

for fileName in testFiles:
    for percentage in errorPercentage:
        createError(fileName, percentage)

        if crc_file_check(fileName.split(".")[0] + "WithErrors." + fileName.split(".")[1]):
            print(fileName, "-> No errors\n")
        else: 
            print(fileName, "-> Errors detected\n")

# c) Aplicação do CRC para os ficheiros produzidos pelo encoder e decoder do módulo 1
testFiles = ["a_encoded.txt", "alice29_encoded.txt", "cp_encoded.htm", "Person_encoded.java", "progc_encoded.c"]

for fileName in testFiles:
    crc_file_compute(fileName)

    if crc_file_check(fileName):
        print(fileName, "-> No errors\n")
    else: 
        print(fileName, "-> Errors detected\n")