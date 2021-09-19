# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper
# case. Executing the program will look as follows:
""""
Text = open('Python Shout.txt')
for i in Text:
    i = i.rstrip()  # strips the newlines from the file
    i = i.upper()
    print(i)
"""

# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: Value and extract it

# Finding Mbox.txt/ txt listed on py4e 
fInput = input("Enter file name ")
fUser = open(fInput)
counter = 0
tot = 0
avg = 0
# loop to go through txt and find "X-DSPAM-Confidence:"
for line in fUser:
    # skips 'uninteresting lines'
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # processes interesting lines
    # calculates total and isolating value after :
    fi = float(line[20:])
    tot = tot + fi
    print(fi)
    counter += 1
    avg = tot / counter

# prints values
print("number of instances:" + str(counter))
print("sum of numbers:" + str(tot))
print("The average is:" + str(avg))

