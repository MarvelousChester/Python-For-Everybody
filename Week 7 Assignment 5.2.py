#  Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate
# message and ignore the number.
# Enter the numbers from the book for problem 5.1 and Match the desired output as shown.

small_num = None
largest_num = None

i = 0
counter = 0
dataset = []
while True:
    userInput = (input("Enter a number:"))
    if userInput == "done" or userInput == "Done":
        break
    try:
        userInput = float(userInput)
        (dataset.append(userInput)) # Forget about this for now as you don't understand lists stuff fully yet
    except:
        print("Invalid input")
        continue
    # this code runs and stores the largest value to largest_num and everytime a new value is put it checks to
    # see if that is largest
    if largest_num is None:
        largest_num = userInput  # assigns largest_num to user input
    elif largest_num < userInput:  # checks if the user input is larger than the current
        largest_num = userInput

    if small_num is None:
        small_num = userInput  # assigns largest_num to user input
    elif small_num > userInput:
        small_num = userInput  # checks if the user input is larger than the current

print(dataset)
print("Largest number is:", float(largest_num))
print("Smallest number is:", float(small_num))
