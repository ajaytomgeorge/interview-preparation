nums = [2, 1, 5, 1, 3, 2]


window_size = 3
window_sum = 0
for i in range(window_size):
    window_sum+=nums[i]

max_value =window_sum

#slide array
for i in range(window_size, len(nums)):
    window_sum+=nums[i]
    window_sum-=nums[i-window_sum]
    max_value = max(max_value,window_sum)


print(max_value)