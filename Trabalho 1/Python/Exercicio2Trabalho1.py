import random
import matplotlib.pyplot as plt

def stringsource(dictionary, probability):
    file = open("stringoutput", 'w')
    result = random.choices(dictionary, weights=probability, k=1000)
    countresults = [0]*len(dictionary)

    idx = 0
    for i in dictionary:
        countresults[idx] = result.count(i)
        idx += 1

    for i in result:
        file.write(i + ";")
    file.close()
    plt.bar(dictionary, countresults, width=0.5)
    plt.show()


stringsource(["aaa", "bbb", "ccc"], [0.25, 0.25, 0.50])
