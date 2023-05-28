import itertools
import string

chars = string.ascii_letters + string.digits
strings = []
for length in range(8, 10):
    for s in itertools.product(chars, repeat=length):
        strings.append(''.join(s))
with open('allStrings.txt', 'w') as f:
    f.write('\n'.join(strings))
print('FINISH!!!')
