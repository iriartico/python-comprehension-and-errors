import sys
import re
import time
import collections

print(sys.path)

text = 'My number phone is 311 123 212, the country code is 591 and my favorite number is 5'
result = re.findall('[0-9]+', text)
print(result)

timestamp = time.time()
local = time.localtime()
format_time = time.asctime(local)
print(format_time)

numbers = [1, 1, 2, 3, 4, 1, 1, 2, 3, 4, 5]
counter = collections.Counter(numbers)
print(counter)
