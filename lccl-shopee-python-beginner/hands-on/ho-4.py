print()

# input
orig_word = input('Enter a word: ')
word = orig_word.lower()

# processing
palindrome = True
for i in range(len(word)//2):
    if word[i] != word[-1 - i]:
        palindrome = False
        break

if palindrome:
    print(f'"{orig_word}" is a palindrome.')
else:
    print(f'"{orig_word}" is NOT a palindrome.')

print()