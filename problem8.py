#Problem 8: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...].
#Write a function cumulative_sum to compute cumulative sum of a list.
#Does your implementation work for a list of strings?

def cumulative_sum(x):
    y = []
    total = x[0]
    y.append(total)
    for i in range(1, len(x)):
        total += x[i]
        y.append(total)
    return y



        