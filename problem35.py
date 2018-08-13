#Problem 35: Write a program to count frequency of characters in a given file.
#Can you use character frequency to tell whether the given file is a Python program file, 
#C program file or a text file?

def read_words(filename):
    return open(filename).read().split()

def char_count(filename):
    y = read_words(filename)
    frequency = {}
    for i in y:
        for char in i:
            frequency[char] = frequency.get(char, 0) + 1
    return frequency
