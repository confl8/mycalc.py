#Ask for first number and store as variable "num1" If it is not a valid variable, the program will
#loop until the correct one is given
num1 = float(input("Please enter a number that is not 0:  "))
while num1 == 0:
    print ('Invalid number! Please choose a valid number')
    num1 = float(input("Please enter a number:  "))

    #Display operations
print("Please select a valid operation:\n1-add\n2-subtract\n3-multiply\n4-divide")

#Prompt for operation. If it is not a valid variable, the program will loop
#until the correct one is given
op_choice = int(input("Please select an operation (1, 2, 3 or 4):  "))

#Prompt for second number and store as variable "num2" If it is not a valid variable,
#the program will loop until the correct one is given
num2 = float(input("Please enter a second number:  "))
while num2 == 0:
    print ('Invalid number! Please choose a valid number that is not 0')
    num2 = float(input("Please enter a number:  "))      



#This part works off of what operation was selected and does the math accordingly
if op_choice == 1:
    result = num1 + num2
elif op_choice == 2:
    result = num1 - num2
elif op_choice == 3:
    result = num1 * num2
elif op_choice == 4:
    result = num1 / num2

#Otherwise exit program
else:
    print("You didn't enter a valid operator")
#Display the result stored in the variable

print(result)

#Exit the program
