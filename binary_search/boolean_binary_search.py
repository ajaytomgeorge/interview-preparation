input_data = [False, False, True, True, True]

start = 0 
end = len(input_data) -1
last_true = 0
while start <= end:
    mid = (start+end) //2
    if input_data[mid] == False:
        start = mid + 1
    if input_data[mid] == True:
        end = mid -1
        last_true = mid


print(last_true)


