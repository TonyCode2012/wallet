import random
import MillerRabinTest
import util

def genRdBigPrime():
    tenThousandPrime = util.generatePrimeByRange(10000)
    bigPrime = util.generateBigPrime()
    tryout = 200000
    tAcc = tryout
    while tAcc >= 0:
        canGetPrime = 'yes'
        for el in tenThousandPrime:
            if bigPrime % el == 0:
                bigPrime += 2
                canGetPrime = 'no'
                break
        if canGetPrime == 'yes':
            break
        tAcc -= 1
    if canGetPrime == 'no':
        print "Having tried", tryout, "times. Can not find prime!!!"
    else:
        return bigPrime 

fileName = ".TMPFILE"
tryout = 1000
tAcc = 0
x = 0
while tAcc < tryout:
    print "Try", tAcc+1, "times to find big prime..."
    x = genRdBigPrime()
    if x != None and MillerRabinTest.miller_rabin_primality_test(x):
        break
    tAcc += 1

if tAcc < tryout:
    print x
    file = open(fileName,'w+')
    file.write(str(x)+"\n")
    file.close()
