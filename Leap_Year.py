# Write a Python program to check whether the given year is leap year or not.

Year= (int(input("Enter the Year:")))

if(Year%4==0 and Year%100!=0):
	    print("It is a leap year")
elif(Year%400==0):
	    print("It is a leap year")
else:
    	print("It is not a leap year")

