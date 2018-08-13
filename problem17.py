#Problem 17: Write a program to print lines of a file in reverse order.

y = open(filename).readlines()
y = y[::-1]
y = ''.join(y)
print(y)

