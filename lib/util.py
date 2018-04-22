import random

def generatePrimeByRange(n):  
    res = []
    flag = [1]*(n+2)  
    p = 2  
    while(p <= n):  
        res.append(p)  
        for i in xrange(2*p,n+1,p):  
            flag[i] = 0  
        while 1:  
            p += 1  
            if(flag[p] == 1):  
                break  
    return res

def generateBigPrime():
    preNum = str(random.randint(1,9))
    count = 0
    numBit = 1024
    while count < numBit:
        preNum += str(random.randint(0,9))
        count += 1
    bigPrime = int(preNum)
    
    if bigPrime % 2 == 1:
        bigPrime += 2

    return bigPrime
