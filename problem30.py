#Problem 30: Write a python function parse_csv to parse csv (comma separated values) files.
#>>> print open('a.csv').read()
#a,b,c
#1,2,3
#2,3,4
#3,4,5
#>>> parse_csv('a.csv')
#[['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]

def parse_csv(filename):
    a = open(filename).read().split()
    b = []
    for i in a:
        i = i.split(',')
        b.append(i)
    return b

print(parse_csv('a.csv'))