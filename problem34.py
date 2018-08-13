#Problem 34: Improve the above program to print the words 
#in the descending order of the number of occurrences.


def read_words(filename):
    return open(filename).read().split()

def frequency(filename):
    y = read_words(filename)
    frequency = {}
    for i in y:
        frequency[i] = frequency.get(i, 0) + 1
    values = []
    for i in frequency.values():
        values.append(i)
    values = sorted(values, reverse=True)
    z = []
    for i in values:
        if i not in z:
            z.append(i)
    words = []
    for i in z:
        for key in frequency:
            if frequency[key] == i:
                words.append(key)
    return words


