#Problem 21: Write a program wrap.py that takes filename and width as aruguments 
#and wraps the lines longer than width.

def wrap(filename, width):
    y = open(filename).readlines()
    for i in y:
        if len(i) > width:
            print(i[0:width], '\n', i[width:])
        else:
            print(i)
            
            
            

