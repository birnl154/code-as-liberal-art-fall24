#I watched a youtube tutorial by Ryan Noonan to help me figure out this assigment since I missed class on wednesday

import collections 
import re

words = re.findall(r'\w+', open('unit-2/script.txt').read().lower())
most_common = collections.Counter(words).most_common(10)
print(most_common)