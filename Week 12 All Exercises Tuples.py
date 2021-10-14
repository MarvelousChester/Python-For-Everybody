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
