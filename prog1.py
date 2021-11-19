# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

# steps
import math
#1 ask for grade percentage
def askGradePercentage():
    _inputGrade = input("Input your grade percentage: ")
    return _inputGrade
#2 convert grade percentage to its equivalent grade. print it with input grade and description.
  # display in the ff. format
  #    Input grade: 
  #    Grade/Mark: 
  #    Description

def convert(inputGrade_):
       # 2.11      Inc. = Incomplete
    if inputGrade_ == 'Inc.':
        print(f" Input Grade: {inputGrade_}\n Grade/Mark: N/A\n Description: Incomplete ")

       # 2.12         W = Withdrawn
    elif inputGrade_ == "W":
        print(f" Input Grade: {inputGrade_}\n Grade/Mark: N/A\n Description: Withdrawn ")

        # 2.13         D = Dropped 
    elif inputGrade == "D":
        print(f" Input Grade: {inputGrade_}\n Grade/Mark: N/A\n Description: Dropped ")

    else:
       # 2.1     97-100 = 1.0   Excellent
        inputGrade_ = float(inputGrade_)
        if round(inputGrade_) >= 97 and round(inputGrade_) <=100:
            print(f" Input Grade: {inputGrade_: .2f}\n Grade/Mark: 1.00\n Description: Excellent ")
    
       # 2.2      94-96 = 1.25  Excellent
        elif round(inputGrade_) >= 94 and round(inputGrade_) <= 96:
            print(f" Input Grade: {inputGrade_: .2f}\n Grade/Mark: 1.25\n Description: Excellent ")

       # 2.3      91-93 = 1.50  Very Good
        elif round(inputGrade_) >= 91 and round(inputGrade_) <= 93:
          print(f" Input Grade: {inputGrade_: .2f}\n Grade/Mark: 1.50\n Description: Very Good ")

       # 2.4      88-90 = 1.75  Very Good
        elif round(inputGrade_) >= 88 and round(inputGrade_) <= 90:
            print(f" Input Grade: {inputGrade_: .2f}\n Grade/Mark: 1.75\n Description: Very Good ")

       # 2.5      85-87 = 2.00  Good
        elif round(inputGrade_) >= 85 and round(inputGrade_) <= 87:
            print(f" Input Grade: {inputGrade_: .2f}\n Grade/Mark: 2.00\n Description: Good ")

       # 2.6      82-84 = 2.25  Good
        elif round(inputGrade_) >= 82 and round(inputGrade_) <= 84:
            print(f" Input Grade: {inputGrade_: .2f}\n Grade/Mark: 2.25\n Description: Good ")

       # 2.7      79-81 = 2.50  Satsifactory
        elif round(inputGrade_) >= 79 and round(inputGrade_) <= 81:
            print(f" Input Grade: {inputGrade_: .2f}\n Grade/Mark: 2.50\n Description: Satisfactory ")

       # 2.8      76-78 = 2.75  Satisfactory
        elif round(inputGrade_) >= 76 and round(inputGrade_) <= 78:
            print(f" Input Grade: {inputGrade_: .2f}\n Grade/Mark: 2.75\n Description: Satisfactory ")

       # 2.9         75 = 3.00  Passing
        elif round(inputGrade_) == 75:
            print(f" Input Grade: {inputGrade_: .2f}\n Grade/Mark: 3.00\n Description: Passing ")

       # 2.10     65-74 = 5.00  Failure
        elif round(inputGrade_) >= 65 and round(inputGrade_) <=74:
            print(f" Input Grade: {inputGrade_: .2f}\n Grade/Mark: 5.00\n Description: Failure ")

        else:
            print("The grade value cannot be categorized. ")


inputGrade = askGradePercentage()
convert(inputGrade)
