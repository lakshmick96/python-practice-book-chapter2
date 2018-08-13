#Problem 38: Write a function invertdict to interchange keys and values in a dictionary.
# For simplicity, assume that all values are unique.

def invertdict(a):
    invert = {}
    key = []
    for i in a.keys():
        key.append(i)
    for i in key:
        invert[a[i]] = i
    return invert


