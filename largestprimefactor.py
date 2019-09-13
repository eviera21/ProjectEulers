# 3. The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
# Difficulty: %5

def LPFF(number): #largest prime factor finder
    factor=0
    for i in range(2,int(number/2)):
        if(number%i==0):
            factor=number/i
            if LPFF(factor)==0:
                break


    return factor

print(LPFF(600851475143))


