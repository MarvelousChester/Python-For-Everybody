# Self Excercise 
# Checks how many times each email is repeated / own excercise for dict()
dates = dict()
text = open("mbox.txt")
for line in text:
    if not line.startswith("From:"):  # for the actual code change it From
        continue
    line = line.rstrip()
    word = line.split()
    for i in word:
        if word not in dates:
            dates[word] = 1
        else:
            dates[word] += 1

print(dates)

# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the
# days of the week. At the end of the program print out the contents of your dictionary (order does not matter). mbox

# For tomorrow Do this again but try first get the amount of times the emails repeat and how many times
# Checks how many times each email is repeated / own exercise for dict()
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
