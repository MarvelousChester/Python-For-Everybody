# Assignment 4.6 Week 6
# https://www.quizerry.com/2020/10/assignment-4-6-week-6-programming-for-everybody-getting-started-with-python-by-coursera/
# My way
def computerPay():
    hrs = float(input("Enter how many hours:"))
    pay = float(input("How much pay hourly:"))
    if hrs > 40:
       pay2 = ((hrs - 40) * (pay * 1.5) + (40 * pay))
       return pay2
    elif hrs <= 40:
        hrs * pay
        return hrs*pay

"""


# Better way to do it

def computerpay(hours, rate):
    print("In computerpay", hours, rate)
    if fh > 40:
        reg = rate*hours
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    print("Returning", pay)
    return pay


sh = input("Enter Hours:")
sr = input("Enter Rate:")
fh = float(sh)  # can do inside of sh
fr = float(sr)  # can do inside of sr

xp = computerpay(fh, fr)
print("Pay:", xp)
