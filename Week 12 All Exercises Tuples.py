# Exercise 1 

# Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of (count,
# email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most
# commits.

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

emails_order = list()
for key, val in (rep.items()):
    order = (val, key)
    emails_order.append(order)

emails_order = sorted(emails_order, reverse=True)

for val, key in emails_order[:10]:
    print(key, val)

# Exercise 2: 
# This program counts the distribution of the hour of the day for each of the messages. You can pull the
# hour from the “From” line by finding the time string and then splitting that string into parts using the colon
# character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour
# as shown below.


time = dict()
txt = open("mbox-short.txt")
lst = list()

# What I tried and didn't work
for line in txt:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    line = line.strip()
    fp = line.find(":")  # Finds what point does the : begin
    hp = line.find(' ', fp) # Finds the end of the portion of time
    host = line[fp-2 : hp]  # Isolates the date to only have time, minute, seconds
    new_line = host.split(":")   # splits data into list
    del new_line[1:3]  # deletes unnecessary minute and seconds

    for i in new_line:
        if i not in time:
            time[i] = 1
        else:
            time[i] += 1


for key, val in (time.items()):
    nums = (val,key)
    lst.append(nums)   # Adds hour and count to list

lst = sorted(lst, reverse=True)  # Puts into order from largest to smallest

for key, val in lst:   # Goes through list and prints it
    print(val, key)


# notes:
# Struggled with this as I the method I used I did not notice that when I used the find method and host I ignored the
# hours and counted minutes and second which took a while to troubleshoot but once fixed it became easier, All I had to
# do was change [fp+1: hp] was to [fp-2: hp] to add the hours from the find
# I saw many other solutions and found them to be shorter and easier to do to my, Below is code from Jmelahman I found

#
# dictionary_hours = dict()               # Initialize variables
# lst = list()
#
# fname = input('Enter file name: ')
# try:
#     fhand = open(fname)
# except FileNotFoundError:
#     print('File cannot be opened:', fname)
#     quit()
#
# for line in fhand:
#     words = line.split()
#     if len(words) < 2 or words[0] != 'From':
#         continue
#
#     col_pos = words[5].find(':')  # Finds the position of the Colon
#     hour = words[5][:col_pos]     # Isolates the block of of texted needed with starting from begining of index 5 and to the position of the colon which is the hour
#     if hour not in dictionary_hours:
#         dictionary_hours[hour] = 1      # First entry
#     else:
#         dictionary_hours[hour] += 1     # Additional counts
#
# for key, val in list(dictionary_hours.items()):
#     lst.append((key, val))              # Fills list with hour, count of dict
#
# lst.sort()                              # Sorts by hour
#
# for key, val in lst:
#     print(key, val)

# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program
# should convert all the input to lower case and only count the letters a-z. Your program should not count spaces,
# digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and
# see how letter frequency varies between languages. Compare your results with the tables at
# https://wikipedia.org/wiki/Letter_frequencies.
import string

bag = dict()
lst = list()

txt = open("Copy.txt")

for line in txt:
    line = line.strip()
    line = line.lower()
    # line.translate(str.maketrans(fromstr, tostr, deletestr)) ,
    # fromstr: list of characters that need to be replaced, tostr: replacer depending on whats written

    line = line.translate(line.maketrans("", "", string.punctuation))
    word = line.split()
    # Make words into letters

    for i in word:
        for letter in i:
            if letter not in bag:
                bag[letter] = 1
            else:
                bag[letter] += 1

# putting into tuple
for key, val in (bag.items()):
    order = (val, key)
    lst.append(order)


# Order and sorting
lst = sorted(lst, reverse=True)
# Printing out the frequencies
for val, key in lst:
    print(key, val)
