# Write a program to read through the mail box data and when you find line that starts with “From”, you will split
# the line into words using the split function. We are interested in who sent the message, which is the second word
# on the From line.

em = open("mbox-short.txt")
who = []
count = 0
for line in em:
    if not line.startswith("From:"):
        continue
    who = line.split()
    count += 1
    print(who[1])
print("The amount of lines are " + str(count))

