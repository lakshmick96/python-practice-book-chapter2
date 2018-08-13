#Problem 6: Write a function reverse to reverse a list. 
#Can you do this without using list slicing?

def reverse(x):
    y = []
    for i in range(len(x)):
        z = x.pop()
        y.append(z)
    return y




    