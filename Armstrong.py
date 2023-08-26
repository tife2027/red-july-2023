# Write a python program to check whether a given three digit number is an Armstrong number.
# A three digit number is said to be an “Armstrong number” 
# if the sum of the third power of its individual digits is equal to the number itself.
#Example: 371 is an Armstrong number as 371 = (3^3) + (7^3) + (1^3)
            #407 is an Armstrong number as 407 = (4^3) + (0^3) + (7^3)

from math import remainder


number= (int(input("Enter the number:")))
temp=number
sum=0

while(number!=0):
    remainder= number%10
    sum=sum + remainder*remainder*remainder
    number= number//10

if(temp==sum):
    print ("This is an Armstrong Number")
else:
    print ("This is not an Armstrong Number")
