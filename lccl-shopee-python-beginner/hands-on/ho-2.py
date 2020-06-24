CENTS_IN_10_DOLLARS = 1000  # Variables with UPPERCASE names
CENTS_IN_5_DOLLARS = 500    # indicate to fellow coders that 
CENTS_IN_2_DOLLARS = 200    # they are constants
CENTS_IN_1_DOLLAR = 100

# input
change = float(input('\nChange ($): '))

# calculations
cents = change * 100

tens = cents // CENTS_IN_10_DOLLARS
cents = cents % CENTS_IN_10_DOLLARS  # cents %= CENTS_IN_10_DOLLARS

fives = cents // CENTS_IN_5_DOLLARS
cents = cents % CENTS_IN_5_DOLLARS

twos = cents // CENTS_IN_2_DOLLARS
cents = cents % CENTS_IN_2_DOLLARS

ones = cents // CENTS_IN_1_DOLLAR
cents = cents % CENTS_IN_1_DOLLAR

c50 = cents // 50
cents = cents % 50

c20 = cents // 20
cents = cents % 20

c10 = cents // 10
cents = cents % 10

# output
print(f'$10 x {tens:.0f}')
print(f'$5  x {fives:.0f}')
print(f'$2  x {twos:.0f}')
print(f'$1  x {ones:.0f}')
print(f'50c x {c50:.0f}')
print(f'20c x {c20:.0f}')
print(f'10c x {c10:.0f}\n')

