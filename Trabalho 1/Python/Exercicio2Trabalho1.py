import random
import matplotlib.pyplot as plt
import string

def stringsource(dictionary, probability, repeat, hist):
    file = open("stringoutput", 'w')
    result = random.choices(dictionary, weights=probability, k=repeat)
    countresults = [0]*len(dictionary)
    idx = 0
    for i in dictionary:
        countresults[idx] = result.count(i)
        idx += 1
    for i in result:
        file.write(i + ";")
    file.close()
    if(hist):
        plt.bar(dictionary, countresults, width=0.5)
        plt.show()
    return result

def passGen(min, max):
    size = random.randint(min, max)
    letters = list(string.ascii_letters + string.digits + string.punctuation)
    probability = [1/len(letters)]*len(letters)
    print(stringsource(letters, probability, size, False))


stringsource(["aaa", "bbb", "ccc", "ddd"], [0.25, 0.25, 0.25, 0.25], 1000, hist=False)
passGen(10, 15)
