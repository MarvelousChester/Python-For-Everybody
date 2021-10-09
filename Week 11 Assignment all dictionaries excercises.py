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
