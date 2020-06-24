print()

total = 0
numbers = []
above_avg = []
below_avg = []

# Get input
while True:
    num = input('Enter a number (blank to quit): ')

    if num == '':
        break

    num = int(num)
    total += num
    numbers.append(num)

if len(numbers) > 0:
    # Processing avaerage and the below- and above- average values
    average = total / len(numbers)
    for num in numbers:
        if num < average:
            below_avg.append(num)
        elif num > average:
            above_avg.append(num)

    # Output
    print(f'Average: {average:.2f}')
    print('Below average:', below_avg)
    print('Above average:', above_avg)

print()