# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the
# numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes

numList = []

while True:
    userInput = input("Enter a number ")

    if userInput == "done" or userInput == "Done":  # Way to exit loop for user
        break
    try:   # fail safe measure to prevent user from inputting something other than int or float
        userInput = float(userInput)
        numList.append(userInput)
    except ValueError:   # gives users feedback that their input is invalid
        print("invalid input")
        continue


print(numList)
print("lowest value:" + str(min(numList)))
print("Highest value:" + str(max(numList)))
