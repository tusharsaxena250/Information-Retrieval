import numpy as np 

#def unique(list1): 
#    x = np.array(list1) 
#    return(np.unique(x)) 
file = [None]*10
for i in range(2):
    file[i] = open("freq-t"+str(i+1)+".txt","r")
    
q =" "
n=10
nw = 
for i in range(2):
    for lines in file[i]:
        line = line.split(":")
        if line[0] not in nw:
            nw = dict(line[0],line[1]) 

def calcw(d):
    temp = unique(d)
    for i in range(0,temp.size):
        if temp[i]=='a':
            nw['a']+=1
        elif temp[i]=='b':
            nw['b']+=1
        elif temp[i]=='c':
            nw['c']+=1
        elif temp[i]=='d':
            nw['d']+=1
        elif temp[i]=='e':
            nw['e']+=1
        elif temp[i]=='f':
            nw['f']+=1
        elif temp[i]=='g':
            nw['g']+=1
        elif temp[i]=='h':
            nw['h']+=1

def calc(d,q):
    temp = unique(d)
    for i in range(temp.size):
        for j in range(q.size):
            if q[j] == d[i]:
    return 

calcw(d1)
calcw(d2)
calcw(d3)
calcw(d4)
calcw(d5)
calcw(d6) 

print(nw)  