import math
import sys

args = sys.argv
contents = []
for i in args:
    contents.extend(i.split("="))

i = 0
while i < len(contents):
    if contents[i] == "--type":
        i += 1
        type = contents[i]
    elif contents[i] == "--payment":
        i += 1
        payment = float(contents[i])
    elif contents[i] == "--principal":
        i += 1
        principal = float(contents[i])
    elif contents[i] == "--periods":
        i += 1
        period = float(contents[i])
    elif contents[i] == "--interest":
        i += 1
        interest = float(contents[i]) / 12 / 100
    else:
        i += 1

if len(contents) < 9:
    print("Incorrect parameters")
elif type != "annuity" and type != "diff":
    print("Incorrect parameters")
elif ('payment' in globals() and payment < 0) or ('principal' in globals() and principal < 0) or ('period' in globals() and period < 0) or ('interest' in globals() and interest < 0):
    print("Incorrect parameters")
elif type == "diff" and 'payment' in globals():
    print("Incorrect parameters")
elif type == "diff":
    m = 1
    sum = 0
    while m <= period:
        D = math.ceil(principal / period + interest * (principal - (principal * (m - 1) / period)))
        print(f"Month {m}: paid out {D}")
        m += 1
        sum += D
    overpayment = sum - principal
    print("")
    print("Overpayment = ", overpayment)
elif type == "annuity":
    if 'payment' not in globals():
        payment = math.ceil(principal * interest * (1 + interest) ** period / ((1 + interest) ** period - 1))
        overpayment = payment * period - principal
        print(f"Your annuity payment = {payment}!")
        print(f"Overpayment = {overpayment}")
    elif 'principal' not in globals():
        principal = payment / (interest * (1 + interest) ** period / ((1 + interest) ** period - 1))
        overpayment = payment * period - principal
        print(f"Your credit principal = {principal}!")
        print(f"Overpayment = {overpayment}")
    elif 'period' not in globals():
        period = math.ceil(math.log((payment / (payment - interest * principal)), (1 + interest)))
        year = period // 12
        month = period % 12
        overpayment = payment * period - principal
        print(f"You need {year} years to repay this credit!")
        print(f"Overpayment = {overpayment}")
    elif 'interest' not in globals():
        print("Incorrect parameters")
