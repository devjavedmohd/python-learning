# targetAge = 90
# currentAge = input('Your current age ')
# yearsLeft = targetAge - int(currentAge)
# monthsLeft = yearsLeft * 12
# daysLeft = yearsLeft * 365
# weeksLeft = yearsLeft * 52
#
# answer = f"You have {daysLeft} days, {weeksLeft} weeks, {monthsLeft} months left."
# print(answer)


# bill = input('What is your total bill amount?')
# percent = input('What percent you want to give as tip ')
# persons = input('How many persons are you? ')
#
# totalTip = int(bill) * (int(percent) / 100)
# print("Total tip amount:", totalTip)
#
# everyOnePay = (float(bill) + float(totalTip)) / int(persons)
#
# print(everyOnePay)

height = int(input('What is your height in cm? '))
print(int(height))
age = int(input('What is your age? '))
print(age)
want_photo = input('Do you want photos shoot? ')

if height < 120:
    print("You can't ride")
elif height > 120:
    print("You can ride")
    if age < 12:
        print('You have to pay $3')
    elif age <= 18:
        print('You have to pay $7')
    else:
        print('You have to pay $12')
if want_photo == 'yes':
    print(f'You have to pay  ')
else:
    print('Total payment')

