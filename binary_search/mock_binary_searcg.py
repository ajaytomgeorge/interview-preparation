input_list= [1,2,3,4,5,6,7,8,9,10]
low =0
end = len(input_list)-1
target = 11
while low < end:
    mid = (low+end)//2
    if target == input_list[mid]:
        print("found break")
        break
    if target < input_list[mid]:
        end = mid -1
    if target > input_list[mid]:
        low = mid +1
print("NOtfOUND")



input_list= [4,5,6,7,8,9,10,1,2,3]
low = 0
end = len(input_list)-1
target = 3
while low< end:
    mid = (low +end)//2:
    if target == input_list[mid]:
        print("Found")
    if input_list[low] < input_list[mid ]:
        if input_list[low] <= target and input_list[mid] > target:
            end = mid -1
        else:
            low = mid +1
    else:
        if input_list[mid] < target and input_list[end] => target:
            low = mid +1
        else:
            end = mid -1