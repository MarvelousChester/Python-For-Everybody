import re

# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a
# regular expression and count the number of lines that matched the regular expression:

count = 0
text = open("mbox.txt")
ad = []
for line in text:
    fin = re.findall("^New revision:, ([0-9].+)",line)
    if not fin:
        continue
    count += 1
    for i in fin:
        a = float(i)
        ad = ad + a
print(count)

# Exercise 2: Write a program to look for lines of the form:
