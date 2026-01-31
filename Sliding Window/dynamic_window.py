from collections import defaultdict
input_data = "abcabcacbb"

left = 0
index_tracker= {}
max_value =0

# check if rpevious occurenace is insdie the window, add one to ethe left point to it place it one string afer the a->left_pointer->bdc
#>= is for initial case aba, left is zero and counter is zero 
for right in range(len(input_data)):
    char = input_data[right]
    if char in index_tracker and index_tracker[char] >= left:
        left = index_tracker[char]+1

    index_tracker[char] = right
    max_value = max(right-left+1, max_value)

print(max_value)