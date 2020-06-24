# input
principal = float(input('\nPrincipal (S$): '))
interest = float(input('Interest (%)  : '))

interest = interest/100 + 1

# output
print(f'Balance after 1st year: S$ {principal*interest:,.2f}')
print(f'Balance after 2nd year: S$ {principal*interest**2:,.2f}')
print(f'Balance after 3rd year: S$ {principal*interest**3:,.2f}\n')
