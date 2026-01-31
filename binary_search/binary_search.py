input_list= [1,2,3,4,5,6,7,8,9,10]
start = 0
end= len(input_list)-1
target =11
while start <= end:
    mid = (end +start) // 2
    print(mid)
    if input_list[mid] == target:
        print("found")
        break
    if input_list[mid] < target:
        start = mid+1
    if input_list[mid] > target:
        end = mid-1


