#Problem 37: Write a function valuesort to sort values of a dictionary based on the key.


def valuesort(a):
    sort_value = []
    key = []
    for i in a.keys():
        key.append(i)
    y = sorted(key)
    for i in y:
        sort_value.append(a[i])
    return sort_value


