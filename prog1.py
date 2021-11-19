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
   # 2.1     97-100 = 1.0   Excellent
def convert(inputGradef):
    inputGrade_ = float(inputGradef)
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
    else: 
        print('others')    

   # 2.7      79-81 = 2.50  Satsifactory
   # 2.8      76-78 = 2.75  Satisfactory
   # 2.9         75 = 3.00  Passing
   # 2.10     65-74 = 5.00  Failure
   # 2.11      Inc. = Incomplete
   # 2.12         W = Withdrawn
   # 2.13         D = Dropped 


inputGrade = askGradePercentage()
convert(inputGrade)