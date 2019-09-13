# 4. A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
# Difficulty: %5

palindrome = 0
for i in range(100,1000):
    for j in range(100,1000):
        number = str(i*j)
        isPal=True
        for k in range(0,int(len(number)/2)):
            if number[k] != number[-1-k]:
                isPal=False
        if isPal and palindrome < i*j:
            palindrome = i*j

print(palindrome)