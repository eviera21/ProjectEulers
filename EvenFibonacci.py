# 2. Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
# Difficulty: %5


num2=0
num1=1
evensum=0
i=0
while(num1<4000000):
    print(str(num2) + "\t"+str(num1)+"\t"+str(num2+num1))
    if num1%2==0:
        evensum+=num1
    num1=num1+num2
    num2=num1-num2
print(evensum)
