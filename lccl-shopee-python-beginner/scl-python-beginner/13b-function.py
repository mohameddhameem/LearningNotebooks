# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

# FUNCTION
# ==========================
print()

def special(s):
    new = ''
    s = s.lower()
    for i, char in enumerate(s):
        if i % 2:   # i % 2 == 1
            char = char.upper()
        new += char
    return new

s = special('Singapore')
print(s)


print()