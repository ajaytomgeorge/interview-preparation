#Problem: Longest Substring Without Repeating Characters
from collections import defaultdict
value =  "abcbacbbeac"

###This find unique not from same

strings = set()
counter = defaultdict(int)
substring = ""
for char in value:
    if counter[char]==1:
        print(counter)
        if substring:
            strings.add(substring)
        counter = defaultdict(int)
        substring = ""
    print(substring)
    counter[char]+=1
    substring += char
strings.add(substring)

print(strings)



