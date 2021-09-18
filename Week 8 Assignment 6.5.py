# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and then use the float
# function to convert the extracted string into a floating point number.

str = 'X-DSPAM-Confidence:0.8475'

print(str.find(":"))
print(str.find("5"))

num = float(str[19:24])  # Another way to do it is by making find(":") a variable and to type [variable name+1:]
# for same result without needing the final digit
print(num)

