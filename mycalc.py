#Ask for first number and store as variable "num1"
num1 = float(input("Please enter a number:  "))

#Display operations
print("Please select a valid operation:\n1-add\n2-subtract\n3-multiply\n4-divide")

#Prompt for operation 
op_choice = int(input("Please select an operation (1, 2, 3 or 4):  "))

#Prompt for second number and store as variable "num2"
num2 = float(input("Please enter a second number:  "))



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

#Display the result
print(result)

