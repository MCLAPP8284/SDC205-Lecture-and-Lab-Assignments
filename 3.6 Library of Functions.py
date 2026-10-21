from datetime import datetime
date = datetime.now()
print(date)

#Function one for the student ID
def functionOne():
    print("My Student ID is miccla8284")

#Function two asks for two numbers & sums them
def functionTwo():
    number1 = int(input("Please enter a whole number: "))
    number2 = int(input("Please enter a whole number: "))
    sumNumber = number1 + number2
    print(f"The sum of n1 and n2 is {sumNumber}")
    return sumNumber

#Function three for if/else on student id numbers
def functionThree(sumNumber):
    if sumNumber > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")
    return 8284

#Main function
def main():
    #Call first function for the student ID informatino
    functionOne()
    #Call second function for the summed amount of the two numbers input
    sumNumber = functionTwo()
    #Call third function to pass the sum and store the ID numbers
    studentID = functionThree(sumNumber)
    #Display the value returned from function three
    print(f"functionThree returned the value of {studentID}")

#Call main to start the program
main()
