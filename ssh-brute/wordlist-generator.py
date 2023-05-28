import random
import string
import time

start_time = time.time()
chars = string.ascii_letters + string.digits
strings = []
for i in range(10):
    length = random.randint(8, 10)
    s = ''.join(random.choice(chars) for _ in range(length))
    strings.append(s)
with open('randomStrings.txt', 'w') as f:
    f.write('\n'.join(strings))
end_time = time.time()
print(f'Time taken: {end_time - start_time} seconds')
print('FINISH!!!')