a = [2,3,4,5,8,9]
target = 7

num_tracker = {}
for id, value in enumerate(a):
    compilment = target - value
    if compilment in num_tracker:
        print( num_tracker[compilment],id)
    num_tracker[value] =id



