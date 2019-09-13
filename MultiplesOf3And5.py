# 1. If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Difficulty: %5
sum=0

for i in range(1,334):
    if 5*i < 1000:
        sum += 5*i
    if 3*i < 1000:
        sum += 3*i
for i in range(0,1000,15):
    sum-=i


print(sum)
