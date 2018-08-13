#Problem 27: Write a function triplets that takes a number n as argument and returns a list of triplets
#such that sum of first two elements of the triplet equals the third element using numbers below n. 
#Please note that (a, b, c) and (b, a, c) represent same triplet.

def triplets(n):
    y = [(x,y,z) for x in range(5) for y in range(5) for z in range(5) if x+y == z]
    for i in y:
        for j in y:
            if sorted(i) == sorted(j):
                y.remove(j)
    return y


        