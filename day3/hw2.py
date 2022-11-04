cents = int(input('Enter the number of cents: '))

nickles = int(input('Enter the number of nickles: '))

dimes = int(input('Enter the number of dimes: '))

quarters = int(input('Enter the number of quarters: '))

cents_as_dollars = cents / 100 

nickles_as_dollars = nickles / 20 

dimes_as_dollars = dimes / 10 

quarters_as_dollars = quarters / 25 

total = cents_as_dollars + nickles_as_dollars + dimes_as_dollars + quarters_as_dollars

print(f'Total of dollars: {total}$')

