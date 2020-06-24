# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

# LIST
# ==========================
print()
# Iterating a list

fruits = ['banana', 'custard apple', 'peach', 'grapes']

for fruit in fruits: 
    print(f'{fruit.capitalize()} is a fruit.')

print('\nGROCERY LIST:')
for i, fruit in enumerate(fruits): 
    print(f'{i+1}. {fruit}')

print()