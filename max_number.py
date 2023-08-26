# Write a Python program to find and display the maximum of three given numbers.

def display(num1, num2, num3):
    message= ""
    if(num1>num2):
        if(num1>num3):
            message= "Number 1 is the greatest"
        else:
            message= "Number 3 is the greatest"
    elif(num2>num3):
        message= "Number 2 is the greatest"
    else:
            message= "Number 3 is the greatest"
    return message

message = display(50,20,150)
print(message)