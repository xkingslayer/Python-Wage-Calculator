####Pay Calculator####
hours_worked = int(input('How many hours did you work this week?'))
hourly_pay = int(input('How much did you make per hour?'))
weeks_per_month = 4

print(f'You made {hours_worked*hourly_pay} this week.')
print(f"You'll make {hourly_pay*hours_worked*weeks_per_month} this month, great job!")
print(f'Please clock in.')

####Clock In Method####
clock_in = int(input('Enter Employee ID:'))
employee_id = 123

if clock_in == employee_id:
    print(f'Correct ID thank you, have a great day!')

else:
    print(f'Incorrect password, you have been locked out.')


