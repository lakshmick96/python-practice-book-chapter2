#Problem 12: 
#Write a function group(list, size) that take a list and splits into smaller lists of given size.

def group(x, n):
   ans = []
   count = len(x)//n
   start = 0
   while count > 0:
       b = []
       for i in range(n):
           b.append(x[start])
           start += 1
       ans.append(b)
       count -= 1
   if len(x)%n != 0:
       b = []
       for i in range(len(x)%n):
           b.append(x[start])
           start += 1
       ans.append(b)
   return ans

