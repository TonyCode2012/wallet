import MillerRabinTest
import util

def findNextPrime():
    tenThousandPrime = util.generatePrimeByRange(10000)
    print "prime range length is:",len(tenThousandPrime)
    filePath = "foundPrime.log"
    pfile = open(filePath)
    prime = int(pfile.readline())
    prime = int(pfile.readline())
    print "prime is:",prime
    pfile.close()
    orgPrime = prime
    prime += 2
    timeAcc = 0
    compAcc = 0
    while 1==1:
        canGetPrime = 'yes'
        for el in tenThousandPrime:
            if prime % el == 0:
                prime += 2
                canGetPrime = 'no'
                break
        if canGetPrime == 'yes' and MillerRabinTest.miller_rabin_primality_test(prime):
            break
        timeAcc += 1
        if timeAcc >= 1000:
            compAcc += timeAcc
            timeAcc = 0
            print "computation times is:",compAcc
    print "distance is:",prime-orgPrime

findNextPrime()
