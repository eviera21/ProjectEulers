# 51. By replacing the 1st digit of the 2-digit number *3, it turns out that six
# of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit,
# this 5-digit number is the first example having seven primes among the ten
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this family, is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
# with the same digit, is part of an eight prime value family.
# Difficulty: %15
def primeNumbersList():
    f = open("primes.txt", "r")
    primesList = f.read().split()
    f.close()
    return primesList

def isPrime(number):
    for i in range(2,int(number/2)):
        if number%i == 0 or number==0:
            return False
    return True
def areEightPrimes(numbers):
    res = 10
    for i in numbers:
        if not isPrime(i):
            res -=1
    return res>=8


def digitChanger(number,changeIn,changeTo):
    nums = list(number)
    for i in range(len(nums)):
        if changeIn[i]=='1':
            nums[i]=str(changeTo)
    return int(''.join(nums))

def replaceTillPrime():
    primesList = primeNumbersList()
    for i in primesList:
        for j in range(1, (2 ** len(i))-1):
            primeFamily = []  # family of numbers to be evaluated
            bincounter = list(bin(j))[2:] #uses binary counting to mark which the current changeable digit
            for k in range(len(i)-len(bincounter)): #adds necessary 0s to match the current prime number
                bincounter = ['0']+bincounter
            for k in range(10): #prepare family of supposed primes
                primeFamily.append(digitChanger(i,bincounter,k))
            print(str(primeFamily)+"\t"+i+"\t"+str(j-1))
            if areEightPrimes(primeFamily): #verifies if the supposed family of primes are actually prime
                return i



print(replaceTillPrime())


