import math


def entropy(filename):
    with open(filename, "rb") as file:
        counters = {byte: 0 for byte in range(2 ** 8)}

        for byte in file.read():
            counters[byte] += 1

        file_size = file.tell()

        probabilities = [counter / file_size for counter in counters.values()]

        entropy = -sum(probability * math.log2(probability) for probability in probabilities if probability > 0)

        print(filename[len("../Test_Output/"):] + ": " + str(entropy))
