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
def lowestOfThree(a_, b_, c_):
    #2.1 If a is the lowest number
    if a_ < b_ and a_ < c_:
        print (f"Lowest Number is {a_}. ")

    #2.2 If b is the lowest number
    elif b_ < a_ and b_ < c_:
        print (f"Lowest Number is {b_}. ")
    
    #2.3 If c is the lowest number
    else:
        print (f"Lowest Number is {c_}. ")
    
a, b, c = askInputs()
#3 display the number with the lowest value
lowestOfThree(a, b, c)