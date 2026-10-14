#Michalle Clapp 10/12/2026
#Guessing game for a number between 0 & 50
#Will loop until the correct nunber is selected
#total number of guesses will be output

#student information
name = input("Please enter your name: ")
studentID = input("Please neter your Student ID: ")

#output to greet the user
print(f"Hello {name}, confirming your Student ID is {studentID}")

#predetermined number
tries = 0
number = 37

#loop for the guess attempts
while True:
    guess = int(input("Enter a number between 0 and 50: "))
    tries += 1

    if guess > number:
        print("You guessed too high.")
    elif guess < number:
        print("You guessed too low.")
    else:
        print(f"Congratulations {name}! You guessed the number in {tries} tries!")
        break

#While loop that runs 5 times
print("\nOutput from the 'while' loop:")
x = number
count = 0

while count < 5:
    x += 1
    print(f"{number} incremented by 1 is {x}")
    count += 1

#For loop that runs 5 times
print("\nOutput from the 'for' loop:")
x = number

for i in range(5):
    x += 1
    print(f"{number} incremented by 1 is {x}")
