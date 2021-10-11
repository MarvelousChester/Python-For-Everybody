# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the
# days of the week. At the end of the program print out the contents of your dictionary (order does not matter). mbox

# Checks dates of email
dates = dict()
text = open("mbox.txt")
for line in text:
    line = line.rstrip()
    word = line.split()
    if len(word) < 3 or word[0] != 'From':  # if the word in the list is less than 3 or word[0] is not
        # from then it continues
        # The strategy I was trying that involved my old ways of doing it caused problem with index out of range 
        # as it pulled out email lists that had no dates thus breaking the code
        # This method that I found online makes it more specific so that it only finds lists with dates 
        continue
    else:
        if word[2] not in dates:
            dates[word[2]] = 1  # first entry
        else:
            dates[word[2]] += 1  # additional counts

print(dates)

# Exercise 3
# Checks how many times each email is repeated / 
rep = dict()
text = open("mbox.txt")
for line in text:
    if not line.startswith("From:"):  # for the actual code change it From
        continue
    line = line.rstrip()
    word = line.split()
    del word[0:1]  # deletes From from being printed it out
    print(word)
    for i in word:
        if i not in rep:
            rep[i] = 1
        else:
            rep[i] += 1
print(dates)

# Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data
# has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5:
# Maximum and minimum loops) to find who has the most messages and print how many messages the person has.


rep = dict()
text = open("mbox.txt")
for line in text:
    if not line.startswith("From:"):  # for the actual code change it From
        continue
    line = line.rstrip()
    word = line.split()
    del word[0:1]  # deletes From from being printed it out and from the list
    for i in word:
        if i not in rep:
            rep[i] = 1
        else:
            rep[i] += 1
print(rep)

# loop method
largest = None
largest_key = None
smallest = None
smallest_key = None

# Finding the largest
for i in rep:
    if largest is None or rep[i] > largest:
        largest = rep[i]
        largest_key = i
# Finding The smallest
for i in rep:
    if smallest is None or rep[i] < smallest:
        smallest = rep[i]
        smallest_key = i

print(largest_key, largest, smallest_key, smallest)
# Easy way to do it
highest = max(rep, key=rep.get,)   # Highest Value name
highest_V = max(rep.values())  # Highest Value int

# print(highest, highest_V)

