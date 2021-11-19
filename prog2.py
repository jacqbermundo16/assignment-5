# Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

# steps
#1 ask for 3 numbers
def askInputs():
    firstNumber = int(input("First Number: "))
    secondNumber = int(input("Second Number: "))
    thirdNumber = int(input("Third Number: "))
    return firstNumber, secondNumber, thirdNumber

#2 create if else statement to determine the lowest number
#3 display the number with the lowest value

a, b, c = askInputs()
print (a)
print (b)
print (c)