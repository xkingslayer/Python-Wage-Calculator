####Pay Calculator####
hoursWorked = int(input('How many hours did you work this week?'))
hourlyPay = int(input('How much did you make per hour?'))
weeksPerMonth = 4

print(f'You made {hoursWorked*hourlyPay} this week.')
print(f"You'll make {hourlyPay*hoursWorked*weeksPerMonth} this month, great job!")
print(f'Please clock in.')

####Clock In Method####
clockIn = int(input('Enter Employee ID:'))
employeeId = 123

if clockIn == employeeId:
    print(f'Correct ID thank you, have a great day!')

else:
    print(f'Incorrect password, you have been locked out.')


